# Conversacion real de ejemplo

## Asistente

Tutor de Matematicas

---

## Modelo base

gemma3:4b

---

## Fecha

2026-08-20

---

# Conversacion

## Usuario

```text
Explica la regla de la cadena
```

---

## Asistente

```text
Okay, vamos a explicar la regla de la cadena.

Imagina que tienes una serie de escaleras que te llevan a un punto final. Cada escalón representa una función y
para llegar al final necesitas subir todos los escalones en secuencia. La regla de la cadena nos da una forma de
calcular el resultado de esa ruta completa, sin tener que calcular cada escalón por separado y luego
multiplicarlos.

Formalmente, si tenemos dos funciones:

*   `g(x)` = f(h(x))
*   Donde `f` y `h` son funciones de una variable, `x`.

La regla de la cadena nos dice que la derivada de `g(x)` con respecto a `x` es igual a la derivada de `f` con
respecto a `h`, multiplicada por la derivada de `h` con respecto a `x`:

d/dx [g(x)] = d/dx [f(h(x))] = f'(h(x)) * h'(x)

En palabras: Primero, calculas la derivada de la función compuesta (la "fuera"). Luego, calculas la derivada de
la función interna (la "dentro"), y finalmente multiplicas los resultados.

Ejemplo numérico:
Digamos que tenemos dos funciones, `f(x) = x^2`  y `h(x) = sin(x)`. Entonces, `g(x) = f(h(x)) = (sin(x))^2`.
Queremos calcular la derivada de `g(x)` con respecto a `x`.

*   Primero calculamos la derivada de `f(x) = x^2`, que es `f'(x) = 2x`.
*   Segundo, calculamos la derivada de `h(x) = sin(x)`, que es `h'(x) = cos(x)`.
*   Finalmente, aplicamos la regla de la cadena:  d/dx [g(x)] = f'(h(x)) * h'(x) = 2 * (sin(x)) * cos(x) = 2
sin(x) cos(x).

Este resultado es el mismo que si calculáramos la derivada de `g(x)` directamente: d/dx [(sin(x))^2] = 2 *
(sin(x))^2 * cos(x).
```
