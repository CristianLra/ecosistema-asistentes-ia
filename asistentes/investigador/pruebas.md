# Pruebas

Este documento registra las pruebas realizadas al asistente.

Su objetivo es verificar que el comportamiento coincide con la especificación definida y detectar oportunidades de mejora.

---

## Prueba 001

### Fecha

2026-08-06

### Versión evaluada

v1.0

### Modelo base

gemma3:4b

### Objetivo

Validar la funcionalidad core: comparación de tecnologías con criterios explícitos.

### Entrada

¿PostgreSQL o MongoDB para un proyecto con muchas relaciones entre tablas?

### Resultado esperado

Comparación con criterios explícitos (tabla o lista), recomendación justificada, sin código.

### Resultado obtenido

Comparó ambas tecnologías con tabla de criterios (tipo de BD, modelado, rendimiento en joins, integridad, escalabilidad, casos de uso), buenas prácticas adicionales, y recomendación clara. Sin código.

### Conclusión

✅ Aprobada.

---

## Prueba 002

### Fecha

2026-08-06

### Versión evaluada

v1.0

### Modelo base

gemma3:4b

### Objetivo

Validar el punto ciego conocido en el ecosistema (código "como ejemplo") en una pregunta mixta: comparación + código.

### Entrada

Compárame Flask con FastAPI y muéstrame un ejemplo de código de cada uno.

### Resultado esperado

Responde la comparación completa (sí le corresponde) y deriva solo la parte de código al Arquitecto Python, sin escribir ningún bloque de código.

### Resultado obtenido

**v1.0:** anunció "derivaré al Arquitecto Python" pero igual entregó los dos bloques de código completos. ❌
**v1.1:** repitió la frase de derivación como texto literal, pero después de haber mostrado el código completo. ❌
**v1.2:** dejó de mostrar código, pero derivó la pregunta entera (incluida la comparación, que sí le correspondía). ⚠️
**v1.3:** respondió la comparación completa con tabla, y derivó únicamente el código con la frase exacta, sin ningún bloque de código. ✅

### Conclusión

✅ Aprobada (en v1.3, tras 3 iteraciones).

---

## Prueba 003

### Fecha

2026-08-06

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar derivación directa cuando la petición es exclusivamente código.

### Entrada

Escríbeme una función en Python que valide un email con regex.

### Resultado esperado

Rechaza escribir código y deriva al Arquitecto Python por nombre, sin versión parcial.

### Resultado obtenido

Derivó de inmediato: "Esa es una pregunta sobre código, me corresponde al Arquitecto Python." Sin código, sin explicación previa.

### Conclusión

✅ Aprobada.

---

## Prueba 004

### Fecha

2026-08-06

### Versión evaluada

v1.1

### Modelo base

gemma3:4b

### Objetivo

Validar derivación de conceptos teóricos de ML, confirmando que el Investigador no hereda el hueco de derivación que persiste en Arquitecto Python v1.2.

### Entrada

¿Qué es el overfitting?

### Resultado esperado

No explica el concepto, deriva al Profesor ML por nombre.

### Resultado obtenido

Derivó de inmediato: "Esa es una pregunta conceptual de Machine Learning, no me corresponde a mí. Te recomiendo consultarlo con el Profesor ML." Sin explicación conceptual.

### Conclusión

✅ Aprobada.

---

# Reevaluaciones

## Reevaluación v1.1

### Motivo

v1.0 anunciaba la derivación pero respondía la parte derivada de todos modos (pruebas 002, 003, 004 fallaban con el mismo patrón).

### Resultado

Se agregó regla explícita ("anunciar la derivación y cumplirla son la misma acción") + ejemplos concretos de pregunta/respuesta esperada. Pruebas 003 y 004 quedaron aprobadas. Prueba 002 (caso mixto) siguió fallando: repitió la frase de ejemplo como texto literal después de mostrar el código completo.

### Estado

⚠️ Parcialmente aprobada.

---

## Reevaluación v1.2

### Motivo

Prueba 002 seguía fallando en v1.1: el ejemplo de texto se copiaba literalmente pero no cambiaba el comportamiento.

### Resultado

Se reemplazó el ejemplo de texto por una regla mecánica ("si hay un bloque de código en el borrador, bórralo antes de responder"). Sobre-corrigió: dejó de mostrar código, pero también dejó de responder la comparación, derivando la pregunta completa.

### Estado

⚠️ Parcialmente aprobada.

---

## Reevaluación v1.3

### Motivo

v1.2 evitaba el código pero también evitaba la comparación que sí le correspondía al Investigador.

### Resultado

Se separó la instrucción en dos pasos obligatorios e independientes (Paso 1: comparación siempre, sin mencionar código ni derivación; Paso 2: evaluar y derivar solo el código). Prueba 002 aprobada: comparación completa con tabla + derivación exacta del código, sin bloques de código.

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

Versión estable.