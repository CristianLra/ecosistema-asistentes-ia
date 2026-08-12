# Automatización de Pruebas

Herramienta que ejecuta las pruebas predeterminadas de los asistentes contra Ollama y
genera reportes reproducibles. Forma parte de la Fase 4 del roadmap.

## Ubicación

- `pruebas/ejecutar_pruebas.py` — runner principal (solo stdlib de Python, sin
  dependencias externas).
- `pruebas/catalogo/<asistente>.json` — definición de las pruebas por asistente.
- `pruebas/reportes/<asistente>/<fecha>.md` — reporte de cada corrida por asistente
  (ignorado por git).
- `pruebas/reportes/resumen-global/<fecha>.md` — resumen de todos los asistentes en una
  misma corrida.

## Cómo se ejecuta

```text
python pruebas/ejecutar_pruebas.py                          # todos los asistentes
python pruebas/ejecutar_pruebas.py --asistente investigador # un asistente
python pruebas/ejecutar_pruebas.py --temperatura 0.8        # ajustar muestreo
python pruebas/ejecutar_pruebas.py --reintentos 2           # 2 reintentos por prueba
python pruebas/ejecutar_pruebas.py --sin-calentamiento      # omitir el calentamiento
python pruebas/ejecutar_pruebas.py --solo-resumen           # regenerar el resumen desde reportes
```

Detalles:

- La temperatura por defecto es `0.0` (greedy) para que los resultados sean
  reproducibles. Las validaciones manuales se hicieron con la temperatura del Modelfile;
  al comparar contra ellas conviene anotar la temperatura usada.
- Antes de cada asistente se envía una petición de calentamiento (prompt breve) para que la
  carga del modelo y su arranque lento no caigan sobre la primera prueba evaluada. Se omite
  con `--sin-calentamiento`.
- Ante un error de conexión (por ejemplo, un primer request colgado en frío), la prueba se
  reintenta hasta `--reintentos` veces (por defecto `1`) antes de registrarse como "no
  ejecutada". Los fallos de criterio no se reintentan.
- `--solo-resumen` regenera `pruebas/reportes/resumen-global/<fecha>.md` a partir del reporte
  más reciente de cada asistente, sin ejecutar pruebas ni requerir Ollama. Útil cuando los
  asistentes se corrieron por separado.
- La salida se escribe por asistente en `pruebas/reportes/<asistente>/<fecha>.md` (cada
  carpeta conserva el historial de corridas de ese asistente), y el resumen global en
  `pruebas/reportes/resumen-global/<fecha>.md`, con la respuesta completa del modelo y el
  detalle de cada criterio. Si una prueba no se ejecuta por un error de conexión, queda
  registrada en la sección "Pruebas no ejecutadas por error" del reporte (y como "no
  ejecutada(s)" en el resumen), para no confundir un reporte parcial con uno completo.
- Requiere Ollama local activo (API en `http://localhost:11434`).

## Formato del catálogo

```json
{
  "asistente": "revisor-codigo",
  "nombre": "Revisor de Código",
  "modelo": "revisor-codigo",
  "modelo_base": "qwen2.5-coder:3b",
  "pruebas": [
    {
      "id": "001",
      "objetivo": "…",
      "entrada": "…",
      "resultado_esperado": "…",
      "criterios": [
        {"tipo": "contiene", "valor": "Arquitecto Python"}
      ]
    }
  ]
}
```

## Criterios verificables

| Tipo | Semántica |
|------|-----------|
| `longitud_minima` | La respuesta alcanza al menos `valor` caracteres. |
| `contiene` | La respuesta contiene el texto `valor`. |
| `no_contiene` | La respuesta no contiene el texto `valor`. |
| `contiene_uno_de` | La respuesta contiene al menos uno de los textos de la lista `valor`. |
| `no_bloques_codigo` | La respuesta no contiene bloques de código (```). |

Los criterios se eligieron para que la verificación sea literal (metodología 4d: palabras
verificables), de modo que la misma prueba pueda ejecutarse por una persona o por el runner.

## Notas operativas

- En esta máquina, ejecutar los 7 asistentes en un solo comando puede tardar mucho tiempo
  (los modelos se cargan y descargan entre asistentes). Se recomienda ejecutar por
  asistente, en particular para iterar.
- Si un proceso se interrumpe, Ollama puede seguir generando la petición pendiente.
  Detenerla con `ollama stop <modelo>`.
- Un criterio que falla puede indicar un problema de comportamiento o un criterio mal
  calibrado. Al ajustar el Modelfile conviene verificar que el fallo desaparece porque el
  comportamiento cambió y no porque el criterio se relajó demasiado.

## Resultado de la primera corrida (2026-08-11)

| Asistente | Resultado | Hallazgo |
|-----------|-----------|----------|
| Tutor de Matemáticas | 5/5 | — |
| Profesor DL | 4/4 | — |
| Profesor ML | 4/4 | — |
| Mentor de Proyectos | 2/2 | — |
| Arquitecto Python | 1/2 | Limitación conocida confirmada (deriva overfitting). |
| Investigador | 3/4 → 4/4 | Rechazaba su funcionalidad core; corregido en v1.4. |
| Revisor de Código | 2/4 → 4/4 | Reescribía código correcto y reconstruía clases; corregido en v1.2. |

## Resultado de la corrida completa (2026-08-12)

Corrida con el runner blindado (calentamiento + reintentos), ejecutada por asistente y
consolidada con `--solo-resumen`:

| Asistente | Resultado | Hallazgo |
|-----------|-----------|----------|
| Tutor de Matemáticas | 5/5 | — |
| Profesor DL | 4/4 | — |
| Profesor ML | 4/4 | — |
| Mentor de Proyectos | 4/4 | — |
| Investigador | 4/4 | — |
| Arquitecto Python | 2/3 | Limitación conocida confirmada (deriva overfitting). Prueba 001 resuelta: el timeout era por falta de calentamiento. |
| Revisor de Código | 4/4 | v1.3: criterio 002 recalibrado y Modelfile reforzado (sin bloques de código en análisis). |

Total: 27/28. A temperatura 0.0 las respuestas no son 100% deterministas: validar con más de
una corrida.
