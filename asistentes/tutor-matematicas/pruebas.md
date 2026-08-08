# Pruebas

Este documento registra las pruebas realizadas al asistente.

Su objetivo es verificar que el comportamiento coincide con la especificación definida y detectar oportunidades de mejora.

---

## Prueba 001

### Fecha

2026-08-07

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar la funcionalidad core: explicación de una herramienta matemática del prerequisito
de ML/DL, sin código ni conceptos de ML/DL.

### Entrada

¿Qué es una derivada?

### Resultado esperado

Explicación con idea central primero, fórmula con el significado de cada término, ejemplo
numérico simple. Sin bloques de código y sin conceptos de ML/DL.

### Resultado obtenido

Explicó la derivada con la idea central primero (tasa de cambio instantánea), fórmula del
límite con el significado de cada término, analogía del coche y ejemplo numérico con
f(x)=x² en x=2. Sin conceptos de ML/DL y sin código (la fórmula se mostró en un bloque
de código solo por renderizado).

### Conclusión

✅ Aprobada.

---

## Prueba 002

### Fecha

2026-08-07

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar el hueco conocido del ecosistema ("código como ejemplo") en una pregunta mixta:
explicación matemática + solicitud de código en la misma consulta.

### Entrada

Explícame qué es el gradiente de una función y muéstrame cómo se calcula en NumPy.

### Resultado esperado

Responde la explicación matemática completa y deriva solo la parte de código al Arquitecto
Python, sin escribir ningún bloque de código.

### Resultado obtenido

Respondió el gradiente completo (paso 1: intuición, notación ∇f con derivadas parciales,
significado de cada término) y derivó solo la parte de código con la frase literal "La
parte del código te la puede mostrar el Arquitecto Python." Cero bloques de código.

**v1.1:** la explicación quedó más limpia que en v1.0 (sin el error "perpendicular a la
tangente" ni la frase confusa del ejemplo), pero sin ejemplo numérico, y mencionó
"descenso del gradiente" como marco al final del paso 1 pese a la prohibición del
Modelfile. Cosmético: no explica el algoritmo.

### Conclusión

✅ Aprobada.

---

## Prueba 003

### Fecha

2026-08-07

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar la derivación de preguntas sobre la aplicación de una técnica de ML al Profesor
ML, aunque la pregunta involucre matemáticas.

### Entrada

¿Por qué el gradiente descendente converge?

### Resultado esperado

No explica el concepto; deriva al Profesor ML nombrándolo explícitamente, y su respuesta
termina ahí.

### Resultado obtenido

Derivó de inmediato: "Esa es una pregunta sobre el comportamiento de un algoritmo de
Machine Learning, no sobre la herramienta matemática en sí. Te recomiendo consultarlo con
el Profesor ML." Sin explicación, sin analogía.

### Conclusión

✅ Aprobada.

---

## Prueba 004

### Fecha

2026-08-07

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar la derivación de conceptos de Deep Learning al Profesor DL, incluso cuando se
expresan en términos matemáticos que el Tutor domina.

### Entrada

¿Qué es backpropagation?

### Resultado esperado

No explica el concepto; deriva al Profesor DL nombrándolo explícitamente, y su respuesta
termina ahí.

### Resultado obtenido

**v1.0:** explicó backpropagation completo (propagación hacia adelante, cálculo del error,
retropropagación, ajuste de parámetros y notación de gradientes). ❌ No derivó.
**v1.1:** derivó de inmediato: "Esa es una pregunta sobre un concepto de Deep Learning, no
sobre la herramienta matemática en sí. Te recomiendo consultarlo con el Profesor DL." ✅

### Conclusión

✅ Aprobada (en v1.1, tras 1 iteración).

---

## Prueba 005

### Fecha

2026-08-07

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar la frontera con estadística: el Tutor domina probabilidad/estadística pero no
explica qué mide una métrica de Machine Learning.

### Entrada

¿Qué mide el F1-score?

### Resultado esperado

No explica la métrica; deriva al Profesor ML nombrándolo explícitamente, y su respuesta
termina ahí.

### Resultado obtenido

Derivó de inmediato: "Esa es una pregunta sobre la aplicación de un concepto de Machine
Learning, no sobre la herramienta matemática en sí. Te recomiendo consultarlo con el
Profesor ML." Sin explicación de la métrica.

### Conclusión

✅ Aprobada.

---

# Reevaluaciones

## Reevaluación v1.1

### Motivo

La prueba 004 fallaba en v1.0: ante "¿Qué es backpropagation?", el Tutor explicó el
concepto completo de Deep Learning en lugar de derivar. La explicación usaba regla de la
cadena y gradientes, herramientas matemáticas que sí le corresponden, lo que reforzó el
hueco.

### Resultado

Se agregó un ejemplo concreto de pregunta/respuesta esperada para DL (backpropagation),
se reforzó el límite de DL mencionando explícitamente que los conceptos de DL se expresan
a menudo con regla de la cadena y gradientes, y se prohibió mencionar nombres de
algoritmos de ML/DL en el paso 1 de las preguntas mixtas. Prueba 004 aprobada; pruebas 001,
003 y 005 sin cambios (ya aprobadas). Prueba 002 mantiene una observación cosmética
(mención de "descenso del gradiente" como marco), no bloqueante.

### Estado

✅ Aprobada.

---

# Resumen de evaluación

| Resultado | Cantidad |
|-----------|---------:|
| ✅ Aprobadas | 5 |
| ⚠️ Mejorables | 0 |
| ❌ No aprobadas | 0 |

## Estado general

Versión estable.
