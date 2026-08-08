# Changelog

Registro de cambios del asistente.

---

## v1.0

### Fecha

2026-08-07

### Cambios

- Primera versión del asistente.
- Definido el rol: explicar el prerequisito matemático de ML/DL (álgebra lineal, cálculo,
  probabilidad y estadística, notación), no el concepto de ML/DL que lo usa.
- Reglas de derivación categóricas incluidas desde el diseño inicial (concepto de ML/DL →
  Profesor ML/DL, código → Arquitecto Python, revisión de código → Revisor de Código,
  planificación → Mentor de Proyectos), aplicando el aprendizaje de los huecos detectados
  en Profesor ML, Profesor DL e Investigador.
- Incluye el patrón de dos pasos obligatorios e independientes para preguntas mixtas
  (matemática + código), tomado de la solución final del Investigador (v1.3).
- Se agregó la frontera de métricas de ML/DL como límite explícito (ej. F1-score), punto
  ciego específico del Tutor por su dominio de estadística.
- Especificación v1 redactada. Pendiente: ejecución de las 5 pruebas base.

---

## v1.1

### Fecha

2026-08-07

### Cambios

- Ronda de pruebas base completada: 5/5 aprobadas.
- La prueba 004 (backpropagation) falló en v1.0: el Tutor explicó el concepto completo de
  Deep Learning en lugar de derivar al Profesor DL, usando la regla de la cadena y los
  gradientes (herramientas matemáticas que sí le corresponden) como justificación.
- Corrección aplicada: ejemplo concreto de pregunta/respuesta esperada para la derivación
  de DL (backpropagation), refuerzo del límite aclarando que los conceptos de DL se
  expresan a menudo con regla de la cadena y gradientes, y prohibición de mencionar
  nombres de algoritmos de ML/DL en el paso 1 de las preguntas mixtas.
- Resultado: prueba 004 aprobada en el primer intento tras la corrección.
- Observación no bloqueante en la prueba 002: menciona "descenso del gradiente" como
  marco de optimización al final del paso 1, pese a la prohibición. Cosmético, no explica
  el algoritmo.
- **Estado: 5/5 pruebas aprobadas. Versión estable.**

---

## Próxima versión

### Mejoras previstas

- Evaluar si conviene cerrar la fuga leve de nombres de algoritmos en el paso 1 de las
  preguntas mixtas (prueba 002) o si se deja como observación aceptada.
- Validar derivaciones a Revisor de Código y Mentor de Proyectos, no cubiertas en las
  pruebas base.
