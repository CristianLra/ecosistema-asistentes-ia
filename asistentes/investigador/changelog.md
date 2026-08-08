# Changelog

Registro de cambios del asistente.

---

## v1.0

### Fecha

2026-08-06

### Cambios

- Primera versión del asistente.
- Definido el rol: investigación técnica sobre librerías, frameworks, comparación de
  tecnologías y buenas prácticas.
- Reglas de derivación categóricas incluidas desde el diseño inicial (código →
  Arquitecto Python, revisión de código → Revisor de Código, teoría de ML/DL →
  Profesor ML/DL, planificación → Mentor de Proyectos), aplicando el aprendizaje de
  los huecos detectados en Profesor ML y Profesor DL (v1.1/v1.2).
- Pruebas iniciales: 1/4 aprobada. Fallo repetido en pruebas 2, 3 y 4: el asistente
  anunciaba la derivación ("Derivaré a...") pero respondía la parte derivada de
  todos modos.

---

## v1.1

### Fecha

2026-08-06

### Cambios

- Corregido el hueco de "anuncia pero no cumple": se agregó la regla explícita de
  que anunciar la derivación y cumplirla son la misma acción, no dos pasos separados.
- Se agregaron ejemplos concretos de pregunta/respuesta esperada para los casos de
  derivación simple y derivación en pregunta mixta (comparación + código).
- Resultado: pruebas 3 y 4 aprobadas. Prueba 2 (caso mixto) seguía fallando — el
  modelo repitió la frase de ejemplo como texto literal, pero después de haber
  mostrado el código completo de todos modos.

---

## v1.2

### Fecha

2026-08-06

### Cambios

- Segundo intento sobre el caso mixto: se reemplazó el ejemplo de texto por una
  regla mecánica ("si hay un bloque de código en el borrador, bórralo antes de
  responder").
- Resultado: dejó de mostrar código, pero sobre-corrigió y derivó la pregunta
  completa, incluyendo la parte de comparación que sí le correspondía. Prueba 2
  quedó en estado mejorable, no aprobada.

---

## v1.3

### Fecha

2026-08-06

### Cambios

- Tercer intento sobre el caso mixto: se separó la instrucción en dos pasos
  obligatorios e independientes (Paso 1: responder siempre la comparación, sin
  mencionar código ni derivación; Paso 2: evaluar si hay código pedido y derivar
  solo esa parte).
- Resultado: prueba 2 aprobada. Comparación completa con tabla + derivación exacta
  del código, sin ningún bloque de código en la respuesta.
- **Estado: 4/4 pruebas aprobadas. Versión estable.**

---

## Próxima versión

### Mejoras previstas

- Evaluar si el Investigador debe derivar hacia un futuro asistente de RAG (Fase 4)
  cuando la pregunta requiera documentación específica del proyecto, en vez de
  conocimiento general del modelo.
- Confirmar con pruebas adicionales (no ejecutadas en esta ronda) las derivaciones a
  Revisor de Código y Mentor de Proyectos, no cubiertas en las 4 pruebas base.