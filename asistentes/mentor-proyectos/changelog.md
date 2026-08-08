# Changelog

## v1.0

### Fecha

2026-08-04

### Cambios

- Primera versión estable del Mentor de Proyectos.
- Especializado en planificación y seguimiento de proyectos.
- Ayuda a organizar el trabajo por etapas.
- Recomienda prioridades.
- Detecta riesgos y bloqueos.
- Integra derivaciones hacia los demás asistentes del ecosistema.
- Modelo base migrado de Qwen2.5-Coder 3B a Gemma 3 4B, siguiendo el criterio de
  `decisiones.md` (Gemma para asistentes consultivos/educativos, no centrados en código).
- Se reforzó la regla de derivación al Arquitecto Python: la instrucción original
  ("Indica que esa tarea corresponde al Arquitecto Python") no era suficiente ante peticiones
  directas de implementación (ej. "Créame una API completa con FastAPI"), y el asistente
  generaba la implementación en lugar de derivar. Se corrigió agregando una regla categórica
  ("NUNCA... sin excepciones") y un ejemplo concreto de la respuesta esperada. Tras el ajuste,
  la derivación se validó correctamente (ver `pruebas.md`, Prueba 003).
- Validado con 4 pruebas (planificación, priorización, derivación al Arquitecto Python,
  seguimiento de proyecto), todas aprobadas.

---

## Próxima versión

### Mejoras previstas

- Añadir y validar una prueba de derivación al Revisor de Código.
- Confirmar que la derivación al Arquitecto Python generaliza ante distintas formulaciones de
  la misma solicitud.
- Vigilar la consistencia del orden de prioridades recomendado entre corridas similares.
- Reforzar que, tras derivar una tarea, el asistente no se acerque a sugerencias de
  implementación (instalación de dependencias, configuración de proyecto, etc.).
