# Pruebas

Este documento registra las pruebas realizadas al Profesor DL.

Su objetivo es verificar que el comportamiento del asistente coincide con la especificación definida y detectar oportunidades de mejora.

---

# Prueba 001

## Fecha

2026-08-03

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Verificar que explique correctamente qué es una red neuronal.

## Entrada

¿Qué es una red neuronal?

## Resultado esperado

Explicar el concepto de forma progresiva, construyendo intuición antes de introducir detalles técnicos.

## Resultado obtenido

En `ollama run` cumplió completamente la estructura esperada.

En Continue respondió mezclando código y explicación.

## Conclusión

✅ Aprobada en Ollama.

⚠️ Continue modifica parcialmente el comportamiento.

---

# Prueba 002

## Fecha

2026-08-03

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Verificar que diferencie correctamente Machine Learning y Deep Learning.

## Entrada

¿Qué diferencia hay entre Machine Learning y Deep Learning?

## Resultado esperado

Relacionar ambos conceptos y explicar claramente sus diferencias.

## Resultado obtenido

Mantiene correctamente su rol.

## Conclusión

✅ Aprobada.

---

# Prueba 003

## Fecha

2026-08-03

## Versión evaluada

v1.0

## Modelo base

gemma3:4b

## Objetivo

Verificar la explicación de Backpropagation.

## Entrada

Explicar Backpropagation.

## Resultado esperado

Construir intuición antes de explicar el algoritmo.

## Resultado obtenido

Comportamiento correcto en Ollama.

## Conclusión

✅ Aprobada.

---

# Prueba 004

## Fecha

2026-08-04

## Versión evaluada

v1.1

## Modelo base

gemma3:4b

## Objetivo

Verificar que el asistente deriva correctamente al Arquitecto Python cuando se le pide
implementar una arquitectura de red neuronal completa.

## Entrada

Impleméntame una red neuronal convolucional completa en PyTorch para clasificar imágenes.

## Resultado esperado

Derivar al Arquitecto Python y explicar el motivo, sin generar código de la arquitectura.

## Resultado obtenido

Derivó explícitamente al Arquitecto Python en el primer párrafo. Explicó el funcionamiento de
una CNN completamente en palabras (sin código) y mantuvo la estructura pedagógica habitual.

Ver `conversaciones/004-derivacion-arquitecto-python.md`.

## Conclusión

✅ Aprobada.

---

# Reevaluaciones

## v1.1

### Motivo

Al agregar la sección de límites al Modelfile (que originalmente no existía, pese a que la
especificación sí la contemplaba), la primera versión de la regla permitía al modelo escribir
código "de ejemplo" o "simplificado". El modelo aprovechó ese margen: reconoció que no debía
generar el proyecto completo, pero de todas formas escribió una clase `SimpleCNN` funcional en
PyTorch, sin derivar al Arquitecto Python.

### Resultado

Se cerró la ambigüedad especificando que no debe escribirse ninguna línea de código de la
arquitectura, sin importar cómo se justifique (proyecto completo, ejemplo, versión básica). Tras
este ajuste, la Prueba 004 se aprobó: derivó correctamente y explicó el concepto solo en
palabras.

### Estado

✅ Aprobada.

---

# Resumen de evaluación

| Resultado | Cantidad |
|-----------|---------:|
| ✅ Aprobadas | 4 |
| ⚠️ Mejorables | 0 |
| ❌ No aprobadas | 0 |

Estado general:

Versión estable (v1.1).
