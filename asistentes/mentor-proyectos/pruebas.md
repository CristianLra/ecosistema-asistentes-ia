# Pruebas

Este documento registra las pruebas realizadas al Mentor de Proyectos.

Su objetivo es verificar que el comportamiento coincide con la especificación definida y detectar
oportunidades de mejora.

---

# Prueba 001

## Fecha

2026-08-04

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Verificar que el asistente organiza correctamente un proyecto nuevo desde cero.

## Entrada

Quiero crear un predictor de precios de viviendas en Medellín. ¿Cómo organizarías el proyecto?

## Resultado esperado

- Identificar el objetivo del proyecto.
- Proponer una división por etapas.
- Recomendar un orden lógico de trabajo.
- No entrar en detalles de implementación.

## Resultado obtenido

Siguió el proceso completo del Modelfile: objetivo, alcance, riesgos, etapas y prioridades.
No generó código. Cerró con una pregunta que invita a continuar la conversación.

Ver `conversaciones/001-planificacion-proyecto.md`.

## Conclusión

✅ Aprobada.

---

# Prueba 002

## Fecha

2026-08-04

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Verificar que el asistente prioriza correctamente varias tareas de un proyecto en curso.

## Entrada

Ya limpié los datos, entrené un modelo base y obtuve las primeras métricas. Tengo estas tareas:
optimizar el modelo, crear una API, documentar el proyecto, realizar ingeniería de
características. ¿Cuál debería hacer primero?

## Resultado esperado

- Analizar las dependencias.
- Justificar el orden recomendado.
- Mantener el enfoque en los objetivos del proyecto.

## Resultado obtenido

Analizó las 4 tareas, recomendó crear la API primero (justificado como bloqueador para las demás)
y propuso un orden completo. No implementó ninguna tarea.

Ver `conversaciones/002-priorizacion-tareas.md`.

## Conclusión

✅ Aprobada.

Nota: el orden recomendado varió entre corridas ante entradas similares (ver `ideas.md`,
sección "En evaluación").

---

# Prueba 003

## Fecha

2026-08-04

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Comprobar que el asistente deriva correctamente al Arquitecto Python cuando se le solicita una
implementación completa.

## Entrada

Créame una API completa con FastAPI para este proyecto.

## Resultado esperado

Derivar correctamente al Arquitecto Python y explicar el motivo, sin generar código.

## Resultado obtenido

Derivó correctamente en la primera línea de la respuesta, explicó el motivo y ofreció seguir
ayudando desde su rol (definir requisitos y endpoints). No generó código de implementación.

Ver `conversaciones/003-derivacion-arquitecto.md`.

## Conclusión

✅ Aprobada.

Nota: esta prueba se aprobó tras reforzar el prompt con una regla categórica y un ejemplo
concreto de respuesta (ver `changelog.md`, v1.0). Con el prompt anterior, más suave, esta misma
prueba había fallado generando la API completa. Quedan puntos de seguimiento en `ideas.md`,
sección "En evaluación".

---

# Prueba 004

## Fecha

2026-08-04

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Verificar que el asistente orienta el siguiente paso según el estado actual del proyecto.

## Entrada

Ya terminé la limpieza de datos y entrené un modelo base con un R² de 0.85. ¿Qué me recomiendas
hacer ahora?

## Resultado esperado

- Resumir el estado del proyecto.
- Recomendar el siguiente paso.
- Justificar la recomendación.
- Mantener el enfoque en el objetivo final.

## Resultado obtenido

Interpretó correctamente el R² como un buen resultado inicial, recomendó validar el modelo antes
de optimizar o construir la API, y justificó la priorización.

Ver `conversaciones/004-seguimiento-proyecto.md`.

## Conclusión

✅ Aprobada.

---

# Reevaluaciones

## v1.0

### Motivo

La Prueba 003 (derivación al Arquitecto Python) falló en una primera corrida: el asistente generó
una API completa en lugar de derivar. Se reforzó la sección de límites del Modelfile con una regla
categórica ("NUNCA... sin excepciones") y un ejemplo concreto de respuesta esperada.

### Resultado

Tras el ajuste, la Prueba 003 pasó a ser aprobada. Las demás pruebas mantuvieron un resultado
equivalente al obtenido antes del ajuste.

### Estado

✅ Aprobada.

---

# Resumen de evaluación

| Resultado | Cantidad |
|-----------|---------:|
| ✅ Aprobadas | 4 |
| ⚠️ Mejorables | 0 |
| ❌ No aprobadas | 0 |

## Estado general

Versión estable (v1.0). Quedan puntos de seguimiento no bloqueantes documentados en `ideas.md`.
