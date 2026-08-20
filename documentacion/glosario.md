# Glosario

Referencia rápida de términos, archivos y diferencias del proyecto.

---

## Estructura del proyecto

### `asistentes/`

Carpeta que contiene los 7 asistentes especializados. Cada uno tiene su propia carpeta con documentación, pruebas y conversaciones.

### `assets/`

Archivos para **demostrar** el proyecto a otros. Contiene conversaciones reales completas (usuario + asistente) que sirven como vitrina de portafolio. Ejemplo: `ejemplo-overfitting.md`.

### `documentacion/`

Documentación general del proyecto: roadmap, versiones, metodología, decisiones, glosario.

### `plantillas/`

Plantillas reutilizables para crear nuevos asistentes. Contiene versiones base de todos los archivos que un asistente necesita (Modelfile, README, especificación, pruebas, etc.).

### `pruebas/`

Sistema de pruebas automatizadas. Contiene el runner, los catálogos de pruebas y los reportes generados.

---

## Archivos clave

### `README.md`

Ficha informativa del proyecto. Orientado a que cualquier persona entienda qué es el proyecto, cómo se usa y cómo se instala. Contiene descripción, instalación, uso y estructura.

### `TODO.md`

Lista de tareas pendientes organizadas por prioridad. Orientado al desarrollador del proyecto, no al usuario.

**Diferencia con README.md:** el README es para quien visita el proyecto; el TODO es para quien lo desarrolla.

---

## Documentación

### `especificacion-v1.md` (en cada asistente)

Documento técnico que define el **contrato** del asistente: qué rol tiene, qué personalidad, cómo responde, qué puede y qué no puede hacer. Es el "manual técnico" del asistente.

**Diferencia con el README del asistente:** la especificación es detallada y técnica (rol, personalidad, límites, integración). El README es un resumen informativo (modelo base, estado, estructura).

### `metodologia-validacion.md`

Responde: ¿**Cómo** valido un asistente? Define el flujo de 8 pasos, los criterios de aprobación y cuándo revalidar.

**Diferencia con automatizacion-pruebas.md:** la metodología es el **proceso** (cómo se hace); la automatización documenta el **runner** y los catálogos JSON.

### `decisiones.md`

Registro formal de decisiones de arquitectura del proyecto. Cada decisión incluye qué se decidió, por qué y en qué fecha.

### `versiones.md`

Historial de versiones de todos los asistentes. Muestra el estado actual de cada uno (v1.0, v1.1, etc.) y limitaciones conocidas.

### `roadmap.md`

Plan de evolución del ecosistema en fases. Muestra qué está completo, qué está en progreso y qué queda pendiente.

### `automatizacion-pruebas.md`

Documentación completa del sistema de pruebas automatizadas: formato de catálogos, criterios verificables, notas operativas y resultados de corridas.

### `glosario.md`

Este archivo. Referencia rápida de términos y diferencias.

---

## Pruebas

### `catalogo/<asistente>.json`

Definición de las pruebas por asistente en formato JSON. Contiene: qué asistente evaluar, qué modelo usar, las preguntas exactas y los criterios verificables por máquina.

**Nota:** JSON no admite comentarios, por eso existe este glosario.

### `ejecutar_pruebas.py`

Runner principal. Consulta la API de Ollama, envía las preguntas del catálogo, evalúa si las respuestas cumplen los criterios y genera reportes markdown. Necesita Ollama activo.

**Diferencia con validar_catalogos.py:** `ejecutar_pruebas.py` ejecuta las pruebas contra Ollama (necesita el modelo corriendo). `validar_catalogos.py` solo verifica que los JSON tengan la estructura correcta (no necesita Ollama).

### `validar_catalogos.py`

Validador de estructura. Verifica que los catálogos JSON tengan todos los campos obligatorios y que los criterios sean válidos. Se ejecuta en CI (GitHub Actions) sin necesidad de Ollama.

**Diferencia con ejecutar_pruebas.py:** este es el "lint" de los catálogos; el otro es el "test runner".

### `__pycache__/`

Carpeta auto-generada por Python cuando se ejecutan scripts. Contiene archivos `.pyc` (código compilado) para acelerar las siguientes ejecuciones. Está en `.gitignore` y no se sube a git.

### `reportes/<asistente>/<fecha>.md`

Salida del runner. Cada corrida genera un reporte por asistente con la respuesta completa del modelo y el detalle de cada criterio. Están en `.gitignore`.

---

## Asistentes

### `conversaciones/` (en cada asistente)

Bitácora de desarrollo. Documenta qué se probó durante la validación, qué pasó, si aprobó o no. Incluye la conversación completa + observaciones + conclusión ("Aprobada"/"Mejorable").

**Diferencia con assets/:** `conversaciones/` es para el desarrollador (bitácora de validación). `assets/` es para el usuario externo (demostración del proyecto).

### `ejemplos/` (en cada asistente)

Casos de prueba definidos: entrada, resultado esperado y criterios de calidad. No son conversaciones reales, sino la **definición** de qué se espera del asistente.

**Diferencia con conversaciones/:** `ejemplos/` es la **definición** (qué se espera). `conversaciones/` es la **ejecución** (qué pasó realmente).

---

## CI/CD

### `validacion.yml`

Archivo de GitHub Actions. Cuando haces push o PR, ejecuta automáticamente: compilación del Python, validación de catálogos JSON y prueba de la ayuda del runner. **No ejecuta pruebas contra Ollama** — eso es solo local.

---

## Modelos

### `Modelfile` (en cada asistente)

Archivo de configuración de Ollama. Define el modelo base, el prompt del sistema (SYSTEM) y los parámetros de temperatura. Se usa con `ollama create` para crear el asistente.

### `gemma3:4b`

Modelo base para asistentes educativos (Profesor ML, Profesor DL, Tutor de Matemáticas). Sigue mejor las instrucciones y mantiene personalidad más consistente.

### `qwen2.5-coder:3b`

Modelo base para asistentes de código (Arquitecto Python, Revisor de Código). Genera mejor código y soluciones técnicas.
