# Ecosistema de Asistentes IA Locales

[![Validación](https://github.com/CristianLra/ecosistema-asistentes-ia/actions/workflows/validacion.yml/badge.svg)](https://github.com/CristianLra/ecosistema-asistentes-ia/actions/workflows/validacion.yml)

Proyecto para desarrollar un ecosistema de asistentes especializados utilizando modelos locales mediante Ollama.

El objetivo es construir asistentes independientes, cada uno con una responsabilidad específica, evitando que un único modelo intente resolver todos los problemas.

Cada asistente deriva las tareas que no le corresponden al asistente especializado adecuado del mismo ecosistema.

```mermaid
graph LR
    U[Usuario] --> T[Tutor de Matemáticas]
    U --> P[Profesor ML]
    U --> D[Profesor DL]
    U --> A[Arquitecto Python]
    U --> R[Revisor de Código]
    U --> M[Mentor de Proyectos]
    U --> I[Investigador]

    T -->|concepto de ML| P
    T -->|concepto de DL| D
    P -->|implementación| A
    D -->|implementación| A
    R -->|desarrollo desde cero| A
    M -->|implementación completa| A
    I -->|concepto de ML| P
    I -->|solo código| A
```

---

## Asistentes

- Profesor ML
- Profesor DL
- Arquitecto Python
- Revisor de Código
- Mentor de Proyectos
- Investigador
- Tutor de Matemáticas

---

## Objetivos

- Especialización.
- Documentación.
- Versionado.
- Validación.
- Evolución continua.

---

## Estructura

- `/asistentes` → Todos los asistentes.
- `/documentacion` → Documentación general.
- `/plantillas` → Plantillas reutilizables.
- `/assets` → Imágenes y diagramas.
- `/pruebas` → Pruebas automatizadas con criterios verificables y reportes reproducibles.

---

## Puesta en marcha

Requisitos: [Ollama](https://ollama.com) y Python 3.

1. Descargar los modelos base y crear los asistentes:

   ```bash
   ollama pull qwen2.5-coder:3b
   ollama pull gemma3:4b

   ollama create arquitecto-python -f asistentes/arquitecto-python/Modelfile
   ollama create investigador -f asistentes/investigador/Modelfile
   ollama create mentor-proyectos -f asistentes/mentor-proyectos/Modelfile
   ollama create profesor-dl -f asistentes/profesor-dl/Modelfile
   ollama create profesor-ml -f asistentes/profesor-ml/Modelfile
   ollama create revisor-codigo -f asistentes/revisor-codigo/Modelfile
   ollama create tutor-matematicas -f asistentes/tutor-matematicas/Modelfile
   ```

2. Probar un asistente:

   ```bash
   ollama run profesor-ml "¿Qué es el overfitting?"
   ```

---

## Pruebas automatizadas

El runner (`pruebas/ejecutar_pruebas.py`, solo stdlib) ejecuta pruebas con criterios verificables por máquina y genera reportes reproducibles por asistente y un resumen global.

```bash
python pruebas/ejecutar_pruebas.py                          # todos los asistentes
python pruebas/ejecutar_pruebas.py --asistente revisor-codigo
python pruebas/ejecutar_pruebas.py --solo-resumen           # regenerar el resumen global
```

Salida de ejemplo:

```text
== Revisor de Código (revisor-codigo) ==
  Calentando modelo revisor-codigo...
  Prueba 001 | consultando...
  ✅ Prueba 001 | Comprobar que identifica correctamente código sin problemas.
  Prueba 002 | consultando...
  ✅ Prueba 002 | Evaluar la calidad de las mejoras propuestas.
  Prueba 003 | consultando...
  ✅ Prueba 003 | Evaluar el análisis de mantenibilidad sin generar una implementación completa.
  Prueba 004 | consultando...
  ✅ Prueba 004 | Comprobar que deriva al Arquitecto Python ante una solicitud de desarrollo desde cero.
```

Un reporte real de ejemplo está en [`pruebas/ejemplo-reporte.md`](pruebas/ejemplo-reporte.md) y la guía completa en [`documentacion/automatizacion-pruebas.md`](documentacion/automatizacion-pruebas.md).

---

## Demo

Una conversación real con el Profesor ML (modelo base `gemma3:4b`) está en [`assets/ejemplo-overfitting.md`](assets/ejemplo-overfitting.md).

---

## Estado del proyecto

Consultar:

documentacion/versiones.md

---

## Licencia

Este proyecto está bajo licencia MIT. Ver `LICENSE` para más detalles.
