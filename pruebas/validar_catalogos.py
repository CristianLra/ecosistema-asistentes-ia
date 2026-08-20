"""Valida la estructura de los catálogos de pruebas sin necesidad de Ollama.

Uso:
    python pruebas/validar_catalogos.py

Salida: 0 si todos los catálogos son válidos, 1 si hay algún error.
"""

import json
import sys
from pathlib import Path

CATALOGO_DIR = Path(__file__).resolve().parent / "catalogo"
CAMPOS_OBLIGATORIOS = ("asistente", "nombre", "modelo", "modelo_base", "pruebas")
# Contrato de validación: define qué tipo de 'valor' admite cada criterio.
# None significa que ese criterio no admite 'valor'.
TIPOS_CRITERIO = {
    "longitud_minima": "numero",
    "contiene": "texto",
    "no_contiene": "texto",
    "contiene_uno_de": "lista",
    "no_bloques_codigo": None,
}


def validar_criterio(criterio, ruta, id_prueba):
    errores = []
    if not isinstance(criterio, dict):
        return [f"{ruta}: Prueba {id_prueba}: criterio debe ser un objeto"]
    tipo = criterio.get("tipo")
    if tipo not in TIPOS_CRITERIO:
        return [f"{ruta}: Prueba {id_prueba}: tipo de criterio desconocido: {tipo}"]
    valor = criterio.get("valor")
    requerido = TIPOS_CRITERIO[tipo]
    if requerido is None:
        if valor is not None:
            errores.append(f"{ruta}: Prueba {id_prueba}: '{tipo}' no admite 'valor'")
    elif requerido == "numero":
        if not isinstance(valor, (int, float)):
            errores.append(f"{ruta}: Prueba {id_prueba}: '{tipo}' requiere un número")
    elif requerido == "texto":
        if not isinstance(valor, str) or not valor:
            errores.append(f"{ruta}: Prueba {id_prueba}: '{tipo}' requiere un texto no vacío")
    elif requerido == "lista":
        if not (isinstance(valor, list) and valor and all(isinstance(v, str) and v for v in valor)):
            errores.append(f"{ruta}: Prueba {id_prueba}: '{tipo}' requiere una lista de textos no vacíos")
    return errores


def validar_archivo(ruta):
    errores = []
    try:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except (json.JSONDecodeError, OSError) as error:
        return [f"{ruta}: JSON inválido: {error}"]
    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in datos:
            errores.append(f"{ruta}: falta el campo '{campo}'")
    pruebas = datos.get("pruebas")
    if not isinstance(pruebas, list) or not pruebas:
        errores.append(f"{ruta}: 'pruebas' debe ser una lista no vacía")
        return errores
    ids = []
    for prueba in pruebas:
        if not isinstance(prueba, dict):
            errores.append(f"{ruta}: cada prueba debe ser un objeto")
            continue
        id_prueba = prueba.get("id")
        if id_prueba in ids:
            errores.append(f"{ruta}: id duplicado: {id_prueba}")
        ids.append(id_prueba)
        for campo in ("id", "objetivo", "entrada", "resultado_esperado", "criterios"):
            if campo not in prueba:
                errores.append(f"{ruta}: la prueba {id_prueba} falta el campo '{campo}'")
        criterios = prueba.get("criterios", [])
        if not isinstance(criterios, list) or not criterios:
            errores.append(f"{ruta}: la prueba {id_prueba} no tiene criterios")
        for criterio in criterios:
            errores.extend(validar_criterio(criterio, ruta, id_prueba))
    return errores


def principal():
    errores = []
    for ruta in sorted(CATALOGO_DIR.glob("*.json")):
        errores.extend(validar_archivo(ruta))
    # El código de salida (0/1) es lo que GitHub Actions interpreta como
    # "pasando"/"fallando" en el paso de validación del workflow.
    if errores:
        for error in errores:
            print(f"ERROR: {error}")
        print(f"\n{len(errores)} error(es).")
        return 1
    cantidad = len(list(CATALOGO_DIR.glob("*.json")))
    print(f"OK: {cantidad} catálogos válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
