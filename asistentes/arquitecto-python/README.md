# Arquitecto Python

Asistente especializado en diseñar software utilizando Python.

---

## Especialidad

- Arquitectura de software.
- Organización de proyectos.
- FastAPI.
- APIs.
- Buenas prácticas.
- Diseño de software.

---

## Responsabilidades

Este asistente puede:

- Diseñar arquitecturas de software.
- Organizar proyectos Python.
- Proponer estructuras de carpetas.
- Recomendar patrones de diseño.
- Generar implementaciones cuando sean necesarias.

---

## No es responsable de

Este asistente NO debe:

- Enseñar Machine Learning.
- Enseñar Deep Learning.
- Revisar código existente.
- Sustituir a otros asistentes especializados.

Cuando una petición corresponda a otro asistente del ecosistema, debe indicarlo de forma breve y derivar al asistente adecuado.

---

## Modelo base

Qwen2.5-Coder 3B

---

## Estado

Versión estable (v1.2), con una limitación conocida documentada.

---

## Limitaciones conocidas

- Ante preguntas conceptuales directas de Machine Learning o Deep Learning (por ejemplo,
  "¿Qué es el overfitting?"), el asistente responde explicando el concepto en lugar de derivar
  al Profesor ML, a pesar de que el Modelfile indica explícitamente que debe derivar.
- Se intentó corregir esta limitación con dos enfoques distintos sobre el prompt (lenguaje
  categórico + ejemplo concreto, y reubicación de la instrucción al inicio del SYSTEM), sin
  éxito en ninguno de los dos casos.
- Esta limitación parece provenir del comportamiento del modelo base (Qwen 2.5 Coder 3B) más
  que del prompt — el modelo tiende a priorizar responder preguntas directas de conocimiento
  general por encima de instrucciones de derivación.
- Se volverá a evaluar cuando se migre a un modelo de mayor capacidad (7B o superior).

Ver `pruebas.md` (Reevaluación v1.2) para el detalle completo.

---

## Estructura

Este asistente contiene:

- README.md
- Modelfile
- especificacion.md
- changelog.md
- ideas.md
- pruebas.md
- ejemplos/
- conversaciones/

---

## Relación con el ecosistema

Este asistente forma parte del Ecosistema de Asistentes IA.

Trabaja junto con:

- Profesor ML
- Profesor DL
- Revisor de Código
- Mentor de Proyectos

---

## Historial

Consultar:

documentacion/versiones.md

---

## Última actualización

2026-08-04
