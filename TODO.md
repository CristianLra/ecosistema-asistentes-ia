# TODO

## Alta prioridad

- [ ] Investigar modelos orientados a arquitectura de software.

---

## Media prioridad

- [ ] Añadir más ejemplos al Profesor ML.
- [x] Documentar la metodología de evaluación de todos los asistentes (ver
      `documentacion/metodologia-validacion.md` y `documentacion/automatizacion-pruebas.md`).

---

## Futuras mejoras

### Revisor de Código

- [x] Reevaluar con Qwen 7B o superior (se resolvió con el prompt en v1.2/v1.3, sin requerir
      un modelo mayor — ver `documentacion/roadmap.md`, Fase 5).
- [ ] Añadir revisión específica para proyectos FastAPI.
- [ ] Añadir revisión específica para proyectos de Machine Learning.
- [ ] Detectar automáticamente code smells.
- [ ] Mejorar la derivación hacia Arquitecto Python.

### Arquitecto Python

- [ ] Reevaluar con Qwen 7B o superior.
- [ ] Añadir más estructuras reutilizables.
- [ ] Incorporar ejemplos mediante RAG.

### Investigador

- [ ] Definir derivación hacia un futuro asistente de RAG (Fase 4) para preguntas que
      requieran documentación específica del proyecto, no solo conocimiento general.
- [ ] Evaluar si el patrón de preguntas mixtas (comparación + código) requiere revisión
      adicional en otros contextos no cubiertos por las 4 pruebas base.

### General

- [ ] Definir criterios de calidad comunes para todos los asistentes.
- [ ] Estandarizar la documentación de futuras versiones.

## Problemas externos

*(Ninguno pendiente — el comportamiento anómalo de Continue fue atribuido a la extensión,
no al Modelfile. Ver documentacion/decisiones.md)*