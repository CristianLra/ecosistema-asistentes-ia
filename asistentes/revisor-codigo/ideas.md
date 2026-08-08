# Ideas

## Pendientes

- Mejorar la detección de code smells.
- Añadir revisión específica para proyectos FastAPI.
- Añadir revisión específica para proyectos de Machine Learning.
- Reevaluar la Prueba 003 (reconstrucción de fragmentos pequeños) con un modelo base de mayor
  capacidad (7B o superior).

---

## En evaluación

- Revisar proyectos completos manteniendo el enfoque de revisión.
- Incorporar listas de verificación según el tipo de proyecto.

---

## Implementadas

- Primera versión del Revisor de Código.
- Revisión centrada en errores y mantenibilidad.
- Evitar reescrituras completas cuando no son necesarias (parcialmente — ver limitación
  conocida en `changelog.md` y `README.md`).
- Separación clara respecto al Arquitecto Python.
- Derivación al Arquitecto Python nombrándolo explícitamente, sin recomendar herramientas
  externas.

---

## Descartadas

- Instrucción genérica de "indicar que corresponde a otro asistente" sin exigir el nombre
  explícito. Se probó en la primera iteración de la Prueba 004 y el modelo derivaba en espíritu
  pero sin nombrar al asistente correcto, o recomendaba herramientas externas.

---

## Aprendizajes para el ecosistema

- Cuando una instrucción de derivación no cede con lenguaje categórico ni con un ejemplo
  concreto, puede ayudar hacerla verificable de forma literal (ej. "tu respuesta debe incluir
  las palabras 'Arquitecto Python'"). Aquí fue el tercer intento el que finalmente funcionó, tras
  dos enfoques más conceptuales que fallaron parcialmente.
