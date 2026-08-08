# Ejemplo 002 - Pregunta mixta: matemática + código

## Objetivo

Validar el hueco conocido del ecosistema ("código como ejemplo") en una pregunta mixta:
explicación matemática + solicitud de código en la misma consulta.

---

## Entrada

```text
Explícame qué es el gradiente de una función y muéstrame cómo se calcula en NumPy.
```

---

## Resultado esperado

- Responde la explicación matemática completa (le corresponde): intuición, notación,
  ejemplo numérico.
- Deriva solo la parte de código al Arquitecto Python, sin escribir ningún bloque de
  código.
- No deriva la pregunta completa: la matemática se responde siempre.

---

## Criterios de calidad

- Explicación del gradiente completa, sin mencionar código ni derivación en esa parte.
- Cero bloques de código en toda la respuesta.
- Frase de derivación que nombra literalmente a "Arquitecto Python".
- No antepone la derivación a la explicación matemática.

---

## Notas

Mismo tipo de falla que quedó como hueco en Profesor ML/DL e Investigador. Se aplica el
patrón de dos pasos obligatorios e independientes que resolvió el caso en el Investigador
v1.3 (Paso 1: matemática siempre; Paso 2: código solo si se pidió, y solo la frase de
derivación).
