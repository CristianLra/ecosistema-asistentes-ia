> Ejemplo de reporte generado por el runner (`pruebas/ejecutar_pruebas.py`) a partir de una
> corrida real del Tutor de Matemáticas (2026-08-12). Los reportes por corrida se generan en
> `pruebas/reportes/<asistente>/<fecha>.md` (no versionados) y se pueden regenerar en
> cualquier momento.

# Reporte de pruebas - Tutor de Matemáticas

Fecha: 2026-08-12 04:03:46

Modelo: tutor-matematicas (base: gemma3:4b)

Temperatura: 0.0

## Resumen

| Prueba | Resultado |
|--------|-----------|
| 001 | ✅ Aprobada |
| 002 | ✅ Aprobada |
| 003 | ✅ Aprobada |
| 004 | ✅ Aprobada |
| 005 | ✅ Aprobada |

Puntuación: 5/5
## Detalle

### Prueba 001 ✅

**Objetivo:** Validar la funcionalidad core: explicación de una herramienta matemática del prerequisito de ML/DL.

**Entrada:**

```text
¿Qué es una derivada?
```

**Resultado esperado:** Explicación con idea central primero, fórmula con el significado de cada término y ejemplo numérico simple. Sin conceptos de ML/DL.

**Criterios:**

- ✅ longitud 1971 >= 250
- ✅ no contiene 'gradiente descendente'
- ✅ no contiene 'backpropagation'

**Respuesta del asistente:**

```text
Esa es una excelente pregunta para empezar. La derivada de una función es un concepto fundamental que, a primera vista, puede parecer complicado, pero su intuición es bastante sencilla.

**Intuición:**

Imagina que estás conduciendo un coche. Tu velocidad en un momento dado es la tasa a la que tu posición cambia con respecto al tiempo. La derivada te da precisamente eso: la *tasa de cambio instantánea* de una función con respecto a una variable (normalmente el tiempo, pero puede ser cualquier otra variable).

Piensa en ello como la pendiente de la línea tangente a la curva de la función en un punto específico.  Si la pendiente es positiva, significa que la función está aumentando en ese punto. Si la pendiente es negativa, significa que la función está disminuyendo. Si la pendiente es cero, significa que la función tiene un punto crítico (un máximo o mínimo local).

**Notación y Formalización:**

Matemáticamente, la derivada de una función *f(x)* con respecto a *x*, denotada como *f'(x)* (se lee "f prima de x"), representa el límite:

f'(x) = lim (h→0) [ f(x + h) - f(x) ] / h

Donde:

*   *f(x)* es la función original.
*   *h* es un cambio infinitesimal en *x*.  Piensa en ello como un incremento muy pequeño de *x*.
*   lim (h→0) significa "el límite cuando *h* se acerca a cero". Esto nos permite calcular la pendiente de la línea tangente cuando el cambio en *x* es infinitamente pequeño.

**Ejemplo Numérico:**

Considera la función f(x) = x².  Si queremos encontrar la derivada de esta función, podemos usar la definición anterior.  En este caso, tenemos:

f'(x) = lim (h→0) [ (x + h)² - x² ] / h
      = lim (h→0) [ x² + 2xh + h² - x² ] / h
      = lim (h→0) [ 2xh + h² ] / h
      = lim (h→0) [ 2x + h ]
      = 2x

Por lo tanto, la derivada de f(x) = x² es f'(x) = 2x.  Esto significa que en cualquier punto *x*, la tasa de cambio instantánea de la función *f(x)* es igual a *2x*.  Si *x* es 1, entonces *f'(1)* = 2.

¿Te parece más claro ahora?

```

### Prueba 002 ✅

**Objetivo:** Validar el hueco de derivación parcial en una pregunta mixta: matemática + código.

**Entrada:**

```text
Explícame qué es el gradiente de una función y muéstrame cómo se calcula en NumPy.
```

**Resultado esperado:** Responder la explicación matemática completa y derivar solo la parte de código al Arquitecto Python, sin bloques de código.

**Criterios:**

- ✅ contiene 'Arquitecto Python'
- ✅ sin bloques de código (```)
- ✅ longitud 1840 >= 200

**Respuesta del asistente:**

```text
Paso 1 — Explicación matemática:

Imagina que tienes una función, digamos f(x), que te da un número como resultado dependiendo del valor que le des a x.  Piensa en esta función como una montaña; el valor de la función es la altura de la montaña en cada punto. El gradiente de esta función en un punto específico 'x' representa la dirección y la magnitud del cambio más pronunciado en la función en ese mismo punto.

Más formalmente, el gradiente es un vector de derivadas parciales.  En una dimensión (un caso especial), el gradiente simplemente es la derivada de la función con respecto a su variable independiente.  Si tienes una función de una sola variable, f(x), su gradiente es simplemente f'(x).  La derivada f'(x) te dice qué tan rápido cambia la función cuando x cambia ligeramente. El valor absoluto de esta derivada indica la *pendiente* de la curva en ese punto; un valor positivo significa que la función está aumentando, y un valor negativo significa que está disminuyendo.

En una dimensión, el gradiente es simplemente el valor de la derivada:  ∇f(x) = f'(x).

Ahora, considera una función de múltiples variables, como f(x, y). El gradiente en este caso es un vector de derivadas parciales: ∇f = (∂f/∂x, ∂f/∂y).  Cada componente del vector representa la derivada parcial de la función con respecto a una variable diferente.  El vector ∇f apunta en la dirección del cambio más rápido de la función y su magnitud indica la tasa de ese cambio.

Por ejemplo, si f(x, y) = x² + y², entonces ∂f/∂x = 2x y ∂f/∂y = 2y. Por lo tanto, ∇f = (2x, 2y).  En el punto (1, 1), el gradiente sería (2, 2), que indica que la función está aumentando más rápidamente en la dirección del vector (1, 1) y que la pendiente de la montaña es la mayor en esa dirección.

Paso 2 — Código:

La parte del código te la puede mostrar el Arquitecto Python.

```

### Prueba 003 ✅

**Objetivo:** Validar la derivación de preguntas sobre la aplicación de una técnica de ML al Profesor ML.

**Entrada:**

```text
¿Por qué el gradiente descendente converge?
```

**Resultado esperado:** No explicar el concepto y derivar al Profesor ML por nombre, terminando ahí.

**Criterios:**

- ✅ contiene 'Profesor ML'
- ✅ no contiene 'convergen'

**Respuesta del asistente:**

```text
Esa es una pregunta sobre el comportamiento de un algoritmo de Machine Learning, no sobre la herramienta matemática en sí. Te recomiendo consultarlo con el Profesor ML.
```

### Prueba 004 ✅

**Objetivo:** Validar la derivación de conceptos de Deep Learning al Profesor DL.

**Entrada:**

```text
¿Qué es backpropagation?
```

**Resultado esperado:** No explicar el concepto (aunque use regla de la cadena/gradientes) y derivar al Profesor DL por nombre, terminando ahí.

**Criterios:**

- ✅ contiene 'Profesor DL'
- ✅ no contiene 'retropropagación'
- ✅ no contiene 'propagación hacia'

**Respuesta del asistente:**

```text
Esa es una pregunta sobre un concepto de Deep Learning, no sobre la herramienta matemática en sí. Te recomiendo consultarlo con el Profesor DL.
```

### Prueba 005 ✅

**Objetivo:** Validar la frontera con estadística: no explicar qué mide una métrica de ML.

**Entrada:**

```text
¿Qué mide el F1-score?
```

**Resultado esperado:** No explicar la métrica y derivar al Profesor ML por nombre, terminando ahí.

**Criterios:**

- ✅ contiene 'Profesor ML'
- ✅ no contiene 'precision'
- ✅ no contiene 'recall'

**Respuesta del asistente:**

```text
Esa es una pregunta sobre la aplicación de un concepto de Machine Learning, no sobre la herramienta matemática en sí. Te recomiendo consultarlo con el Profesor ML.
```
