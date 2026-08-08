# Pruebas

Este documento registra las pruebas realizadas al Profesor ML.

Su objetivo es verificar que el comportamiento del asistente coincide con la especificación definida y detectar oportunidades de mejora.

---

# Prueba 001

## Fecha

2026-08-04

## Versión evaluada

v1.2

## Modelo base

gemma3:4b

## Objetivo

Verificar que el asistente explique correctamente qué es Machine Learning siguiendo la estructura pedagógica definida.

## Entrada

¿Qué es Machine Learning?

## Resultado esperado

- Responder en español.
- Crear contexto antes de definir el concepto.
- Explicar el problema que resuelve.
- Dar una definición clara.
- Utilizar al menos un ejemplo sencillo.
- Evitar un estilo enciclopédico.
- Finalizar con una pregunta breve.

## Resultado obtenido

Siguió la estructura completa de 6 pasos (problema, definición, ejemplo intuitivo del niño y las
manzanas, funcionamiento, aplicaciones, limitaciones). Cerró con pregunta de comprobación.

Ver `conversaciones/001-que-es-machine-learning.md`.

## Conclusión

✅ Aprobada.

---

# Prueba 002

## Fecha

2026-08-04

## Versión evaluada

v1.2

## Modelo base

gemma3:4b

## Objetivo

Comprobar que el asistente explica el overfitting construyendo primero la intuición.

## Entrada

¿Qué es el overfitting?

## Resultado esperado

- Explica el problema que representa el overfitting.
- Construye una intuición mediante un ejemplo sencillo.
- Define el concepto.
- Explica por qué ocurre.
- Menciona formas comunes de reducirlo.

## Resultado obtenido

Reutilizó la analogía del niño y las manzanas (ahora con manzanas rojas y redondas) para
construir intuición antes de definir el concepto técnicamente. Explicó causas y mencionó
regularización y aumento de datos como mitigación.

Ver `conversaciones/002-que-es-el-overfitting.md`.

## Conclusión

✅ Aprobada.

---

# Prueba 003

## Fecha

2026-08-04

## Versión evaluada

v1.2

## Modelo base

gemma3:4b

## Objetivo

Comprobar que el asistente explica un algoritmo clásico (regresión lineal) siguiendo su
metodología de enseñanza.

## Entrada

Explícame qué es la regresión lineal.

## Resultado esperado

- Explica qué problema resuelve.
- Define el concepto.
- Utiliza un ejemplo sencillo.
- Explica cómo funciona.
- Menciona aplicaciones reales.
- Explica sus limitaciones.

## Resultado obtenido

Siguió la estructura completa. Usó el ejemplo de predecir el precio de una casa según su tamaño,
introdujo la fórmula `y = mx + b` de forma acotada y como apoyo, no como sustituto de la
explicación conceptual.

Ver `conversaciones/003-regresion-lineal.md`.

## Conclusión

✅ Aprobada.

---

# Prueba 004

## Fecha

2026-08-04

## Versión evaluada

v1.2

## Modelo base

gemma3:4b

## Objetivo

Verificar que el asistente deriva correctamente al Arquitecto Python cuando se le pide una
implementación completa, sin escribir código.

## Entrada

Impleméntame un modelo de regresión lineal completo, listo para producción, con validación
cruzada y todo.

## Resultado esperado

Derivar al Arquitecto Python y explicar el motivo, sin generar código de la implementación.

## Resultado obtenido

Derivó al Arquitecto Python en la primera línea. Explicó las 5 etapas del proceso (división de
datos, entrenamiento, validación cruzada, ajuste de hiperparámetros, evaluación final)
completamente en palabras, sin ningún bloque de código.

Ver `conversaciones/004-derivacion-arquitecto-python.md`.

## Conclusión

✅ Aprobada.

---

# Reevaluaciones

## v1.1

### Motivo

La única prueba registrada en v1.0 (Prueba 001) había quedado como ⚠️ Mejorable: no creaba
contexto antes de definir, no usaba ejemplo intuitivo, y la respuesta se parecía a la de un
asistente general. Se ajustó el Modelfile: español obligatorio, se reforzó el comportamiento de
profesor particular, se evitó el estilo enciclopédico y se mejoró la estructura.

### Resultado

No quedó documentada una reevaluación formal de la Prueba 001 en ese momento.

### Estado

Sin verificar formalmente hasta la reevaluación v1.2.

---

## v1.2

### Fecha

2026-08-06

### Motivo

Antes de correr ninguna prueba, se detectó que `pruebas.md` solo tenía un resultado registrado
(v1.0) y ningún ejemplo ni prueba cubría la derivación hacia otros asistentes del ecosistema. Se
reforzó preventivamente la sección de límites del Modelfile con lenguaje categórico y un ejemplo
concreto de derivación (aplicando el aprendizaje obtenido con Profesor DL), y se creó el ejemplo
004 de derivación al Arquitecto Python.

### Resultado

- Pruebas 001, 002 y 003 (conceptuales): aprobadas con la versión reforzada del Modelfile,
  resolviendo también los puntos que habían quedado pendientes desde v1.0.
- Prueba 004 (derivación) requirió dos intentos:
  - Primer intento: el asistente reconoció verbalmente que la implementación completa
    correspondía al Arquitecto Python, pero de inmediato entregó una guía "paso a paso" con 7
    bloques de código funcionales — el mismo tipo de hueco que ya se había visto en Profesor DL,
    aunque bajo una etiqueta distinta ("guía", no "ejemplo").
  - Segundo intento: se cerró explícitamente ese hueco, indicando que ni siquiera una guía paso
    a paso puede incluir bloques de código. Con este ajuste, la Prueba 004 se aprobó: derivó
    correctamente y explicó el proceso completo solo en palabras.

### Estado

✅ Aprobada. 4 de 4 pruebas aprobadas.

---

# Resumen de evaluación

| Resultado | Cantidad |
|-----------|---------:|
| ✅ Aprobadas | 4 |
| ⚠️ Mejorables | 0 |
| ❌ No aprobadas | 0 |

Estado general:

Versión estable (v1.2).
