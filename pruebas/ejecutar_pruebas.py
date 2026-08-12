"""Ejecuta las pruebas predeterminadas de los asistentes del ecosistema contra Ollama.

Las pruebas se definen en catalogo/<asistente>.json con criterios verificables por
máquina. El script consulta la API local de Ollama, evalúa cada criterio y genera un
reporte en markdown por asistente.

Uso:
    python ejecutar_pruebas.py
    python ejecutar_pruebas.py --asistente tutor-matematicas
    python ejecutar_pruebas.py --asistente revisor-codigo --temperatura 0.7
    python ejecutar_pruebas.py --url http://localhost:11434
"""

import argparse
import json
import sys
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CATALOGO_DIR = BASE_DIR / "catalogo"
REPORTES_DIR = BASE_DIR / "reportes"
URL_BASE = "http://localhost:11434"
ENDPOINT_GENERAR = "/api/generate"
ENDPOINT_MODELOS = "/api/tags"


@dataclass
class Criterio:
    tipo: str
    valor: object = None


@dataclass
class Prueba:
    id: str
    objetivo: str
    entrada: str
    resultado_esperado: str
    criterios: list = field(default_factory=list)


@dataclass
class ResultadoCriterio:
    criterio: Criterio
    aprobado: bool
    detalle: str


@dataclass
class ResultadoPrueba:
    prueba: Prueba
    respuesta: str
    criterios: list = field(default_factory=list)

    @property
    def aprobada(self):
        return all(c.aprobado for c in self.criterios)


def cargar_catalogos(directorio):
    catalogos = []
    for archivo in sorted(directorio.glob("*.json")):
        datos = json.loads(archivo.read_text(encoding="utf-8"))
        pruebas = [
            Prueba(
                id=p["id"],
                objetivo=p["objetivo"],
                entrada=p["entrada"],
                resultado_esperado=p["resultado_esperado"],
                criterios=[Criterio(c["tipo"], c.get("valor")) for c in p["criterios"]],
            )
            for p in datos["pruebas"]
        ]
        catalogos.append(
            {
                "archivo": archivo,
                "asistente": datos["asistente"],
                "nombre": datos["nombre"],
                "modelo": datos["modelo"],
                "modelo_base": datos["modelo_base"],
                "pruebas": pruebas,
            }
        )
    return catalogos


def verificar_conexion(url_base):
    try:
        urllib.request.urlopen(url_base + ENDPOINT_MODELOS, timeout=10)
        return True
    except Exception:
        return False


def consultar_ollama(modelo, prompt, url_base, temperatura, timeout):
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperatura},
    }
    datos = json.dumps(payload).encode("utf-8")
    peticion = urllib.request.Request(
        url_base + ENDPOINT_GENERAR,
        data=datos,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(peticion, timeout=timeout) as respuesta:
            cuerpo = json.loads(respuesta.read().decode("utf-8"))
    except Exception as error:
        return None, str(error)
    return cuerpo.get("response", ""), None


def evaluar_criterio(criterio, respuesta):
    tipo = criterio.tipo
    valor = criterio.valor
    texto = respuesta.lower()
    if tipo == "longitud_minima":
        aprobado = len(respuesta) >= valor
        detalle = f"longitud {len(respuesta)} >= {valor}"
    elif tipo == "contiene":
        aprobado = valor.lower() in texto
        detalle = f"contiene '{valor}'"
    elif tipo == "no_contiene":
        aprobado = valor.lower() not in texto
        detalle = f"no contiene '{valor}'"
    elif tipo == "contiene_uno_de":
        aprobado = any(v.lower() in texto for v in valor)
        detalle = f"contiene al menos uno de: {valor}"
    elif tipo == "no_bloques_codigo":
        aprobado = "```" not in respuesta
        detalle = "sin bloques de código (```)"
    else:
        aprobado = False
        detalle = f"tipo de criterio desconocido: {tipo}"
    return ResultadoCriterio(criterio, aprobado, detalle)


def ejecutar_prueba(prueba, modelo, url_base, temperatura, timeout):
    respuesta, error = consultar_ollama(modelo, prueba.entrada, url_base, temperatura, timeout)
    if error is not None:
        return None, error
    criterios = [evaluar_criterio(c, respuesta) for c in prueba.criterios]
    return ResultadoPrueba(prueba, respuesta, criterios), None


def imprimir_prueba(resultado):
    marca = "✅" if resultado.aprobada else "❌"
    fallos = [c.detalle for c in resultado.criterios if not c.aprobado]
    detalle = f"  ({'; '.join(fallos)})" if fallos else ""
    print(f"  {marca} Prueba {resultado.prueba.id} | {resultado.prueba.objetivo}{detalle}")


def bloquear_texto(texto):
    return f"```text\n{texto}\n```"


def generar_reporte(catalogo, resultados, fecha, temperatura, errores=None):
    errores = errores or []
    aprobadas = sum(1 for r in resultados if r.aprobada)
    total = len(resultados)
    lineas = [f"# Reporte de pruebas - {catalogo['nombre']}", ""]
    lineas.append(f"Fecha: {fecha}")
    lineas.append("")
    lineas.append(f"Modelo: {catalogo['modelo']} (base: {catalogo['modelo_base']})")
    lineas.append("")
    lineas.append(f"Temperatura: {temperatura}")
    lineas.append("")
    lineas.append("## Resumen")
    lineas.append("")
    lineas.append("| Prueba | Resultado |")
    lineas.append("|--------|-----------|")
    for r in resultados:
        marca = "✅ Aprobada" if r.aprobada else "❌ No aprobada"
        lineas.append(f"| {r.prueba.id} | {marca} |")
    lineas.append("")
    lineas.append(f"Puntuación: {aprobadas}/{total}")
    if errores:
        lineas.append("")
        lineas.append("## Pruebas no ejecutadas por error")
        lineas.append("")
        for prueba_id, error in errores:
            lineas.append(f"- Prueba {prueba_id}: {error}")
        lineas.append("")
    lineas.append("## Detalle")
    lineas.append("")
    for r in resultados:
        marca = "✅" if r.aprobada else "❌"
        lineas.append(f"### Prueba {r.prueba.id} {marca}")
        lineas.append("")
        lineas.append(f"**Objetivo:** {r.prueba.objetivo}")
        lineas.append("")
        lineas.append(f"**Entrada:**")
        lineas.append("")
        lineas.append(bloquear_texto(r.prueba.entrada))
        lineas.append("")
        lineas.append(f"**Resultado esperado:** {r.prueba.resultado_esperado}")
        lineas.append("")
        lineas.append("**Criterios:**")
        lineas.append("")
        for c in r.criterios:
            marca_c = "✅" if c.aprobado else "❌"
            lineas.append(f"- {marca_c} {c.detalle}")
        lineas.append("")
        lineas.append("**Respuesta del asistente:**")
        lineas.append("")
        lineas.append(bloquear_texto(r.respuesta))
        lineas.append("")
    return "\n".join(lineas)


def configurar_consola():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, UnicodeError):
        pass


def generar_resumen_global(resumenes, fecha, temperatura):
    lineas = ["# Resumen global de pruebas", ""]
    lineas.append(f"Fecha: {fecha}")
    lineas.append("")
    lineas.append(f"Temperatura: {temperatura}")
    lineas.append("")
    lineas.append("| Asistente | Puntuación |")
    lineas.append("|-----------|-----------|")
    for nombre, aprobadas, total, errores in resumenes:
        marca = "✅" if aprobadas == total else "❌"
        extra = f" ⚠️ {errores} no ejecutada(s)" if errores else ""
        lineas.append(f"| {nombre} | {marca} {aprobadas}/{total}{extra} |")
    lineas.append("")
    total_aprobadas = sum(a for _, a, _, _ in resumenes)
    total_pruebas = sum(t for _, _, t, _ in resumenes)
    lineas.append(f"Total: {total_aprobadas}/{total_pruebas}")
    return "\n".join(lineas)


def resumen_desde_reportes(reportes_dir, fecha_legible):
    """Reconstruye el resumen global a partir del reporte más reciente de cada asistente."""
    resumenes = []
    for carpeta in sorted(reportes_dir.iterdir()):
        if not carpeta.is_dir() or carpeta.name == "resumen-global":
            continue
        reportes = sorted(carpeta.glob("*.md"))
        if not reportes:
            continue
        texto = reportes[-1].read_text(encoding="utf-8")
        nombre = None
        temperatura = "0.0"
        aprobadas = total = 0
        errores = 0
        for linea in texto.splitlines():
            if linea.startswith("# Reporte de pruebas - "):
                nombre = linea[len("# Reporte de pruebas - "):]
            elif linea.startswith("Temperatura: "):
                temperatura = linea[len("Temperatura: "):]
            elif linea.startswith("Puntuación: "):
                partes = linea[len("Puntuación: "):].split("/")
                aprobadas = int(partes[0])
                total = int(partes[1])
            elif linea.startswith("- Prueba ") and ":" in linea:
                errores += 1
        if nombre is not None:
            resumenes.append((nombre, aprobadas, total, errores, temperatura))
    if not resumenes:
        return None, "0.0"
    temperatura_global = resumenes[0][4]
    resumenes = [r[:4] for r in resumenes]
    return generar_resumen_global(resumenes, fecha_legible, temperatura_global), temperatura_global


def principal(argv=None):
    configurar_consola()
    parser = argparse.ArgumentParser(
        description="Ejecuta las pruebas de los asistentes contra Ollama y genera reportes."
    )
    parser.add_argument(
        "--asistente",
        default="todos",
        help="Asistente a evaluar (nombre del archivo en catalogo/, sin .json). Por defecto: todos.",
    )
    parser.add_argument(
        "--modelo",
        default=None,
        help="Sobrescribir el nombre del modelo en Ollama (por defecto, el del catálogo).",
    )
    parser.add_argument(
        "--url",
        default=URL_BASE,
        help=f"URL base de la API de Ollama. Por defecto: {URL_BASE}.",
    )
    parser.add_argument(
        "--temperatura",
        type=float,
        default=0.0,
        help="Temperatura de muestreo. 0.0 (defecto) da respuestas deterministas.",
    )
    parser.add_argument(
        "--tiempo-limite",
        type=int,
        default=1200,
        help="Tiempo máximo en segundos por petición a Ollama. Por defecto: 1200.",
    )
    parser.add_argument(
        "--reintentos",
        type=int,
        default=1,
        help="Reintentos por prueba ante errores de conexión. Por defecto: 1.",
    )
    parser.add_argument(
        "--sin-calentamiento",
        action="store_true",
        help="Omitir la petición de calentamiento previa a cada asistente.",
    )
    parser.add_argument(
        "--directorio-catalogo",
        default=str(CATALOGO_DIR),
        help=f"Directorio con los catálogos de prueba. Por defecto: {CATALOGO_DIR}.",
    )
    parser.add_argument(
        "--directorio-reportes",
        default=str(REPORTES_DIR),
        help=f"Directorio de salida de los reportes. Por defecto: {REPORTES_DIR}.",
    )
    parser.add_argument(
        "--solo-resumen",
        action="store_true",
        help="Regenerar el resumen global a partir del reporte más reciente de cada asistente "
        "sin ejecutar pruebas ni requerir Ollama.",
    )
    args = parser.parse_args(argv)

    if args.solo_resumen:
        reportes_dir = Path(args.directorio_reportes)
        if not reportes_dir.is_dir():
            print(f"Error: no existe el directorio de reportes {reportes_dir}.")
            sys.exit(1)
        fecha = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        fecha_legible = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resumen, _ = resumen_desde_reportes(reportes_dir, fecha_legible)
        if resumen is None:
            print(f"Error: no hay reportes en {reportes_dir}.")
            sys.exit(1)
        print(resumen)
        directorio_resumen = reportes_dir / "resumen-global"
        directorio_resumen.mkdir(parents=True, exist_ok=True)
        archivo_resumen = directorio_resumen / f"{fecha}.md"
        archivo_resumen.write_text(resumen, encoding="utf-8")
        print(f"\nResumen global: {archivo_resumen}")
        sys.exit(0)

    if not verificar_conexion(args.url):
        print(f"Error: no se pudo conectar con Ollama en {args.url}. Verifica que esté en ejecución.")
        sys.exit(1)

    catalogos = cargar_catalogos(Path(args.directorio_catalogo))
    if not catalogos:
        print(f"Error: no hay catálogos en {args.directorio_catalogo}.")
        sys.exit(1)

    if args.asistente != "todos":
        catalogos = [c for c in catalogos if c["asistente"] == args.asistente]
        if not catalogos:
            disponibles = ", ".join(c["asistente"] for c in cargar_catalogos(Path(args.directorio_catalogo)))
            print(f"Error: no se encontró catálogo para '{args.asistente}'. Disponibles: {disponibles}.")
            sys.exit(1)

    fecha = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    fecha_legible = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reportes_dir = Path(args.directorio_reportes)
    reportes_dir.mkdir(parents=True, exist_ok=True)

    resumen_global = []
    for catalogo in catalogos:
        modelo = args.modelo or catalogo["modelo"]
        print(f"\n== {catalogo['nombre']} ({modelo}) ==")
        if not args.sin_calentamiento:
            print(f"  Calentando modelo {modelo}...")
            consultar_ollama(modelo, "Hola", args.url, args.temperatura, args.tiempo_limite)
        resultados = []
        errores = []
        for prueba in catalogo["pruebas"]:
            resultado, error = None, None
            for intento in range(1, args.reintentos + 2):
                print(f"  Prueba {prueba.id} | consultando...")
                resultado, error = ejecutar_prueba(prueba, modelo, args.url, args.temperatura, args.tiempo_limite)
                if error is None:
                    break
                if intento <= args.reintentos:
                    print(f"  Reintento {prueba.id} {intento}/{args.reintentos}...")
            if error is not None:
                errores.append((prueba.id, error))
                print(f"  ⚠️ Prueba {prueba.id} | error al consultar Ollama: {error}")
                continue
            resultados.append(resultado)
            imprimir_prueba(resultado)
        if not resultados and not errores:
            continue
        aprobadas = sum(1 for r in resultados if r.aprobada)
        resumen_global.append((catalogo["nombre"], aprobadas, len(resultados), len(errores)))
        reporte = generar_reporte(catalogo, resultados, fecha_legible, args.temperatura, errores)
        directorio_asistente = reportes_dir / catalogo["asistente"]
        directorio_asistente.mkdir(parents=True, exist_ok=True)
        nombre_archivo = directorio_asistente / f"{fecha}.md"
        nombre_archivo.write_text(reporte, encoding="utf-8")
        print(f"  Reporte: {nombre_archivo}")

    print("\n== Resumen global ==")
    print("| Asistente | Puntuación |")
    print("|-----------|-----------|")
    for nombre, aprobadas, total, errores in resumen_global:
        marca = "✅" if aprobadas == total else "❌"
        extra = f"  ⚠️ {errores} no ejecutada(s)" if errores else ""
        print(f"| {nombre} | {marca} {aprobadas}/{total}{extra} |")
    total_aprobadas = sum(a for _, a, _, _ in resumen_global)
    total_pruebas = sum(t for _, _, t, _ in resumen_global)
    print(f"\nTotal: {total_aprobadas}/{total_pruebas}")

    if len(resumen_global) > 1:
        resumen = generar_resumen_global(resumen_global, fecha_legible, args.temperatura)
        directorio_resumen = reportes_dir / "resumen-global"
        directorio_resumen.mkdir(parents=True, exist_ok=True)
        archivo_resumen = directorio_resumen / f"{fecha}.md"
        archivo_resumen.write_text(resumen, encoding="utf-8")
        print(f"Resumen global: {archivo_resumen}")


if __name__ == "__main__":
    principal()
