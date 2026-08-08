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

## Próxima versión

### Mejoras previstas

- Detectar más patrones de code smells.
- Añadir revisión de proyectos completos.
- Reevaluar la Prueba 003 al migrar a un modelo base de mayor capacidad (7B o superior).
