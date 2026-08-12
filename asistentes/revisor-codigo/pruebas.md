# Pruebas

Este documento registra las pruebas realizadas al Revisor de Código.

Su objetivo es verificar que el comportamiento del asistente coincide con la especificación definida y detectar oportunidades de mejora.

---

# Prueba 001

## Fecha

2026-08-06

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Comprobar que identifica correctamente código sin problemas.

## Entrada

```text
¿Ves algún problema en este código?

def suma(a, b):
    return a + b

print(suma(5, 3))
```

## Resultado esperado

Detectar que el código es correcto y evitar cambios innecesarios.

## Resultado obtenido

Identificó correctamente que el código no presenta problemas. No inventó errores ni propuso
cambios innecesarios.

## Conclusión

✅ Aprobada.

---

# Prueba 002

## Fecha

2026-08-06

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Evaluar la calidad de las mejoras propuestas.

## Entrada

```text
¿Cómo mejorarías este código?

x = []

for i in range(100):
    x.append(i)
```

## Resultado esperado

Proponer mejoras pequeñas y justificadas sin reescribir completamente el código.

## Resultado obtenido

Propuso la comprensión de listas (`[i for i in range(100)]`), justificó brevemente el cambio y
mantuvo el mismo objetivo del código. Mejoró respecto a la evaluación anterior, donde había
tendido a reestructurar más código del necesario.

## Conclusión

✅ Aprobada.

---

# Prueba 003

## Fecha

2026-08-06

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Evaluar el análisis de mantenibilidad sin generar una implementación completa.

## Entrada

```text
¿Qué problemas de mantenibilidad tiene este código?

class Usuario:

    pass
```

## Resultado esperado

Detectar problemas de mantenibilidad sin generar una implementación completa.

## Resultado obtenido

Detectó correctamente la falta de funcionalidad y listó problemas de mantenibilidad válidos
(documentación, métodos sin implementación, etc.), pero volvió a generar una implementación
completa de la clase (constructor, método `saludar`, docstrings, ejemplo de uso), a pesar de que
el Modelfile indica explícitamente limitarse al fragmento proporcionado.

## Conclusión

❌ No aprobada. Documentada como limitación conocida del modelo base (ver `README.md` y
`changelog.md`, sección "Limitaciones conocidas").

---

# Prueba 004

## Fecha

2026-08-06

## Versión evaluada

v1.1

## Modelo base

qwen2.5-coder:3b

## Objetivo

Comprobar que deriva correctamente al Arquitecto Python, nombrándolo explícitamente, ante una
solicitud de desarrollo de software desde cero.

## Entrada

```text
Créame una API completa con FastAPI.
```

## Resultado esperado

Derivar la tarea al Arquitecto Python, nombrándolo explícitamente, sin recomendar herramientas
externas ni ofrecer guiar la implementación.

## Resultado obtenido

Derivó correctamente, mencionando "Arquitecto Python" de forma explícita, sin ofrecer guiar la
estructura ni ejemplos de código, y cerrando con la oferta de revisar el código cuando exista.

## Conclusión

✅ Aprobada (ver Reevaluaciones — requirió 3 iteraciones del Modelfile).

---

# Reevaluaciones

## v1.1

### Fecha

2026-08-06

### Motivo

Se detectó que `pruebas.md` reflejaba resultados de una versión anterior del Modelfile
(2026-08-03), previos a las correcciones ya incorporadas ("no señales problemas que no existan",
"limítate a analizar el fragmento"). Además, en la Prueba 004 se identificó que, aunque el
asistente rechazaba correctamente crear la API, recomendaba herramientas externas (Copilot,
Codex, contratar un desarrollador) en lugar de derivar al Arquitecto Python.

### Resultado

- Pruebas 001 y 002: se revalidaron y aprobaron con el Modelfile ya corregido previamente.
- Prueba 003: se revalidó; el problema de reconstrucción completa persiste sin cambios respecto
  a la evaluación anterior. Se confirma como limitación del modelo base, no del prompt.
- Prueba 004: requirió tres iteraciones del Modelfile:
  1. Se agregó la instrucción de nombrar al Arquitecto Python y prohibir herramientas externas.
     Resultado: dejó de mencionar herramientas externas, pero tampoco nombró al Arquitecto
     Python; en su lugar ofreció guiar la estructura del proyecto él mismo.
  2. Se agregó la exigencia explícita de incluir literalmente las palabras "Arquitecto Python" y
     la prohibición de ofrecer guía o ejemplos de código en ese momento.
     Resultado: aprobada. Derivó correctamente, nombrando al Arquitecto Python y sin ofrecer
     ayuda adicional fuera de su rol.

### Estado

✅ 3 de 4 pruebas aprobadas. Prueba 003 documentada como limitación conocida.

---

## v1.2

### Fecha

2026-08-11

### Motivo

La automatización de pruebas (Fase 4) detectó dos fallos reproducibles no registrados en la
validación manual de v1.1: la Prueba 001 reescribía código correcto con una "versión
mejorada", y la Prueba 003 seguía reconstruyendo la clase vacía de forma intermitente.

### Resultado

- Primera corrección: prohibir mejoras estéticas y reescrituras sobre código correcto.
  Prueba 001 aprobada y Prueba 003 aprobada (dejó de generar `def __init__` y `def saludar`),
  pero se sobre-corrigió: la Prueba 002 dejó de proponer mejoras cuando el usuario las pedía
  explícitamente.
- Segunda corrección: se reestructuró la regla como árbol de decisión según la pregunta del
  usuario (opinión/detección de problemas → confirmar y detenerse; petición explícita de
  mejoras → proponer). Prueba 002 volvió a proponer mejoras concretas.

### Estado

✅ 4/4 pruebas aprobadas. La Prueba 003 deja de ser limitación conocida: la reconstrucción
de fragmentos pequeños se resolvió con el prompt y no requirió un modelo de mayor capacidad.

---

## v1.3

### Fecha

2026-08-12

### Motivo

Nuevas corridas automatizadas con el mismo catálogo, Modelfile y temperatura (0.0) dieron
resultados distintos: la corrida del 2026-08-11 15:51 dio 4/4 y la del 2026-08-12 04:00 dio
2/4. Se confirma que las respuestas no son 100% deterministas aunque la temperatura sea 0.0.

### Resultado

- Prueba 002: el criterio era demasiado frágil. El asistente propuso una mejora válida
  (`x = list(range(100))`, "versión mejorada") pero sin ninguna frase de la lista original. Se
  amplió la lista de `contiene_uno_de` con "versión mejorada", "se puede mejorar", "mejorada",
  "más concisa" y "más eficiente".
- Prueba 003: el asistente reconstruyó la clase vacía con `def __init__` y un bloque de código
  completo. El comportamiento intermitente que v1.2 había resuelto reapareció. Se reforzó el
  Modelfile prohibiendo bloques de código cuando el usuario solo pide análisis u opinión y
  prohibiendo explícitamente escribir la clase reescrita.
- Se recreó el modelo (`ollama create revisor-codigo -f Modelfile`).

### Estado

✅ 4/4 pruebas aprobadas en dos corridas consecutivas (2026-08-12 04:24 y 04:25). Se mantiene
la observación de no determinismo a temperatura 0.0: conviene validar con más de una corrida.

---

# Resumen de evaluación

| Resultado | Cantidad |
|-----------|---------:|
| ✅ Aprobadas | 4 |
| ⚠️ Mejorables | 0 |
| ❌ No aprobadas | 0 |

Estado general:

Versión estable (v1.3), sin limitaciones conocidas. Nota: a temperatura 0.0 las respuestas
pueden variar entre corridas; validar con más de una corrida.
