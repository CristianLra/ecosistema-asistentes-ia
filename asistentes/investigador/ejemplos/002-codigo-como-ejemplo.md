# Ejemplo 002 - Código como ejemplo (punto ciego conocido)

## Objetivo

Verificar que el Investigador no cae en el hueco ya detectado en Profesor ML y
Profesor DL: usar código "como ejemplo ilustrativo" para completar una respuesta
que en el fondo pertenece a otro asistente.

---

## Entrada

​```text
Compárame Flask con FastAPI y muéstrame un ejemplo de código de cada uno.
​```

---

## Resultado esperado

- Responde la comparación (sí le corresponde).
- Se detiene antes de la parte de código y deriva esa parte al Arquitecto Python,
  nombrándolo explícitamente.
- No genera código, ni siquiera una versión "simplificada" o "solo para ilustrar".

---

## Criterios de calidad

- Cero líneas de código en la respuesta.
- Nombra a "Arquitecto Python" de forma literal.
- La parte de comparación sí se responde completa.

---

## Notas

Prueba de mayor prioridad: replica el tipo de hueco que costó dos iteraciones
corregir en Profesor ML y Profesor DL.