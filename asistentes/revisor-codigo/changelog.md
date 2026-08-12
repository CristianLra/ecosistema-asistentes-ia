# Changelog

Registro de cambios del Revisor de Código.

---

## v1.0

### Fecha

2026-08-03

### Cambios

- Primera versión estable del Revisor de Código.
- Especializado en revisar código existente.
- Detecta errores, problemas de diseño y mantenibilidad.
- Evita cambios innecesarios cuando el código ya es correcto.
- No cambia el lenguaje utilizado por el usuario.
- Deriva el desarrollo de software nuevo al Arquitecto Python.
- Se agregaron las instrucciones "no señales problemas que no existan" y "limítate a analizar el
  fragmento proporcionado" para reducir alucinaciones y reescrituras innecesarias.

### Limitaciones conocidas

- En ocasiones genera implementaciones completas cuando el usuario solicita revisar un fragmento
  pequeño de código (ver Prueba 003), a pesar de la instrucción explícita de limitarse al
  fragmento.
- Este comportamiento parece deberse al modelo base (Qwen2.5-Coder 3B) y no al prompt: persiste
  igual tras la revalidación de v1.1.
- Se reevaluará al migrar a modelos de mayor capacidad.

---

## v1.1

### Fecha

2026-08-06

### Cambios

- Se revalidaron las 4 pruebas con el Modelfile ya corregido en v1.0 (el registro anterior
  reflejaba una versión previa a esas correcciones).
- Prueba 002 mejoró de ⚠️ Mejorable a ✅ Aprobada.
- Se detectó que la Prueba 004 (derivación) rechazaba correctamente crear software nuevo, pero
  recomendaba herramientas externas (Copilot, Codex, contratar un desarrollador) en lugar de
  derivar al Arquitecto Python. Se corrigió en dos iteraciones:
  1. Prohibir explícitamente herramientas externas y exigir nombrar al Arquitecto Python
     (resultado parcial: dejó de recomendar herramientas externas, pero tampoco nombró al
     Arquitecto Python, y ofreció guiar la implementación él mismo).
  2. Exigir que la respuesta incluya literalmente las palabras "Arquitecto Python" y prohibir
     ofrecer guía o ejemplos de código en el momento de derivar (resultado: aprobada).
- Prueba 003 se mantiene como limitación conocida, sin cambios respecto a v1.0.

---

## v1.2

### Fecha

2026-08-11

### Cambios

- Automatización de pruebas (Fase 4) detectó dos fallos reproducibles:
  - Prueba 001: reescribía código correcto con una "versión mejorada" (docstrings, nombres
    de variables), contradiciendo la instrucción de evitar cambios innecesarios.
  - Prueba 003: seguía reconstruyendo la clase vacía con constructor y métodos completos.
- Fix en dos iteraciones:
  1. Se prohibió proponer mejoras estéticas ni reescrituras sobre código correcto. Resultado:
     la Prueba 003 dejó de reconstruir la clase, pero se sobre-corrigió: la Prueba 002
     (petición explícita de mejoras) también dejó de proponerlas.
  2. Se reestructuró la regla como árbol de decisión según la pregunta del usuario: opinión/
     detección de problemas → confirmar y detenerse; petición explícita de mejoras → proponer
     mejoras concretas. Resultado: 4/4 pruebas aprobadas.
- La Prueba 003 deja de ser limitación conocida: la reconstrucción de clases vacías se
  resolvió con el prompt y no requirió un modelo de mayor capacidad.

---

## v1.3

### Fecha

2026-08-12

### Cambios

- La automatización detectó que, a temperatura 0.0, las respuestas no son 100% deterministas:
  una corrida (2026-08-11) dio 4/4 y otra (2026-08-12) dio 2/4 con el mismo catálogo y Modelfile.
- Prueba 002: el criterio era demasiado frágil. El asistente propuso una mejora válida
  (`x = list(range(100))`) pero sin ninguna de las frases de la lista (`comprensión de listas`,
  `sugiero`, etc.). Se amplió la lista con las frases que usa naturalmente ("versión mejorada",
  "se puede mejorar", "mejorada", "más concisa", "más eficiente").
- Prueba 003: volvió a reconstruir la clase vacía con `def __init__` (comportamiento
  intermitente que v1.2 no eliminó por completo). Se reforzó el Modelfile: prohibido incluir
  bloques de código cuando el usuario solo pide análisis u opinión, y prohibido escribir la
  clase reescrita en las respuestas de mantenibilidad.
- Resultado: 4/4 aprobadas en dos corridas consecutivas (2026-08-12 04:24 y 04:25).

---

## Próxima versión

### Mejoras previstas

- Detectar más patrones de code smells.
- Añadir revisión de proyectos completos.
- Reevaluar la Prueba 003 al migrar a un modelo base de mayor capacidad (7B o superior).
