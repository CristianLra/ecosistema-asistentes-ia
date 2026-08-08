# Changelog

Registro de cambios del Profesor ML.

---

## v1.0

### Fecha

2026-08-03

### Cambios

- Creación del Profesor ML.
- Especialización en Machine Learning.
- Metodología basada en comprensión profunda.
- Separación respecto a otros asistentes.
- Definición del uso de ejemplos y código.
- Incorporación de comprobaciones de aprendizaje.
- Definición de límites del asistente.

---

## v1.1

### Fecha

2026-08-03

### Cambios

- El español pasa a ser el idioma obligatorio.
- Se refuerza el comportamiento como profesor particular.
- Se evita el estilo enciclopédico.
- Mejora la estructura de las explicaciones.
- Se incorporan ejemplos intuitivos.
- Se añaden preguntas de comprobación cuando aportan valor.

---

## v1.2

### Fecha

2026-08-06

### Cambios

- Se detectó que `pruebas.md` solo tenía un resultado registrado desde v1.0, y que no existía
  ninguna prueba de derivación hacia otros asistentes del ecosistema.
- Se reforzó la sección de límites del Modelfile con lenguaje categórico y un ejemplo concreto
  de cómo derivar al Arquitecto Python.
- Primer intento: el asistente derivaba verbalmente pero entregaba una guía "paso a paso" con
  código funcional completo — un hueco similar al detectado antes en Profesor DL, con una
  etiqueta distinta.
- Segundo intento: se cerró explícitamente ese hueco (ninguna guía puede incluir bloques de
  código). Con este ajuste, la derivación se validó correctamente.
- Se añadió el ejemplo `ejemplos/004-derivacion-arquitecto-python.md`, que no existía antes.
- Se revalidaron las Pruebas 001, 002 y 003, todas aprobadas con la versión reforzada del
  Modelfile.

---

## Próxima versión

### Mejoras previstas

- Adaptar mejor la profundidad al nivel del estudiante.
- Incorporar más ejercicios prácticos.
- Confirmar que la derivación al Arquitecto Python generaliza ante otras formas de pedir
  implementación (no solo regresión lineal).
