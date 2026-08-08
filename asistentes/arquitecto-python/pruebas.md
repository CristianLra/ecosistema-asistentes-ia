# Pruebas

Este documento registra las pruebas realizadas al Arquitecto Python.

Su objetivo es verificar que el comportamiento del asistente coincide con la especificación definida y detectar oportunidades de mejora.

---

# Prueba 001

## Fecha

2026-08-03

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Verificar la generación de una API básica.

## Entrada

Crea una API básica con FastAPI.

## Resultado esperado

- Generar una API funcional.
- Código limpio.
- Lista para ejecutar.

## Resultado obtenido

- API funcional.
- Código correcto.
- Explicación breve.

## Conclusión

✅ Aprobada.

---

# Prueba 002

## Fecha

2026-08-03

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Evaluar la organización de un proyecto de Machine Learning.

## Entrada

Organizar un proyecto de Machine Learning.

## Resultado esperado

- Proponer una estructura moderna.
- Seguir buenas prácticas.
- Organizar correctamente las carpetas.

## Resultado obtenido

- Propuso una estructura aceptable.
- No utilizó exactamente la estructura definida para el proyecto.

## Conclusión

⚠️ Mejorable.

---

# Prueba 003

## Fecha

2026-08-03

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Comprobar la separación entre Arquitecto Python y Profesor ML.

## Entrada

¿Qué es el overfitting?

## Resultado esperado

Derivar la explicación conceptual al Profesor ML y ofrecer ayuda únicamente para implementarlo en Python.

## Resultado obtenido

Explicó completamente el concepto.

## Conclusión

❌ No respetó completamente su rol.

---

# Reevaluaciones

## v1.1

### Motivo

Mejorar el enfoque arquitectónico.

### Resultado

Las respuestas mejoraron considerablemente.

Ahora identifica mejor los requisitos antes de implementar.

Todavía existe una ligera tendencia a implementar soluciones completas debido al comportamiento del modelo base.

### Estado

✅ Aprobada.

---

## v1.2

### Fecha

2026-08-04

### Modelo base

qwen2.5-coder:3b

### Motivo

La Prueba 003 seguía fallando en v1.1: el asistente explicaba conceptos de Machine Learning en
lugar de derivarlos al Profesor ML. Se intentaron dos correcciones sucesivas sobre el prompt:

1. Reforzar la instrucción con lenguaje categórico ("NUNCA... sin excepciones") y un ejemplo
   concreto de la respuesta esperada.
2. Mover esa sección de límites al inicio del prompt, por si el orden influía en el peso que el
   modelo le da a la instrucción.

### Resultado

- Prueba 001 (API con FastAPI): se mantuvo aprobada, con una respuesta incluso más completa
  (incluyó una alternativa justificada con path operation decorators).
- Prueba 002 (organización de proyecto ML): mejoró de ⚠️ Mejorable a ✅ Aprobada — la
  estructura propuesta pasó de 6 a 9 fases, bien justificadas, sin generar código.
- Prueba 003 (derivación al Profesor ML): **siguió fallando** con ambas correcciones. El
  asistente volvió a explicar el concepto completo de overfitting (definición, señales de
  detección, técnicas de mitigación), sin mencionar al Profesor ML en ningún momento.

### Interpretación

A diferencia de las fallas de tipo "generar una implementación cuando debía derivar" (que sí se
corrigieron con este mismo enfoque en otros asistentes del ecosistema, como el Mentor de
Proyectos), esta falla es de otra naturaleza: el usuario hace una pregunta directa de
conocimiento general ("¿Qué es X?"), y el modelo prioriza responderla por encima de la
instrucción del SYSTEM. Esto no cedió ni reforzando el lenguaje de la instrucción ni cambiando su
posición en el prompt — dos palancas distintas, mismo resultado.

Siguiendo la distinción de `documentacion/metodologia-validacion.md` entre limitaciones del
SYSTEM y limitaciones del modelo base, esto se interpreta como una **limitación del modelo base**
(qwen2.5-coder:3b) y no del prompt.

### Estado

✅ Aprobada parcialmente (2 de 3 pruebas). Se documenta la Prueba 003 como limitación conocida
en lugar de seguir iterando sobre el prompt (ver `README.md`, sección "Limitaciones conocidas").

---

# Resumen de evaluación

| Resultado | Cantidad |
|-----------|---------:|
| ✅ Aprobadas | 2 |
| ⚠️ Mejorables | 0 |
| ❌ No aprobadas | 1 |

## Estado general

Versión estable (v1.2), con una limitación conocida documentada. Pendiente de reevaluación
cuando se migre a un modelo base de mayor capacidad (7B o superior).
