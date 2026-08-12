# Roadmap

## Fase 1 - Fundación ✅

- [x] Estructura del proyecto
- [x] Sistema de plantillas
- [x] Documentación base
- [x] Profesor ML
- [x] Arquitecto Python

---

## Fase 2 - Asistentes principales ✅

- [x] Revisor de Código
- [x] Profesor DL
- [x] Mentor de Proyectos

---

## Fase 3 - Asistentes de apoyo ✅

- [x] Investigador
- [x] Tutor de Matemáticas

---

## Fase 4 - Ecosistema

- [ ] Sistema RAG
- [ ] Coordinador
- [ ] Biblioteca de ejemplos
- [x] Automatización de pruebas

> La automatización de pruebas quedó operativa (ver
> `documentacion/automatizacion-pruebas.md`). Ha detectado y ayudado a resolver
> comportamientos no registrados en las validaciones manuales: el Investigador rechazaba su
> funcionalidad core (comparación de tecnologías), el Revisor de Código reescribía código
> correcto (v1.2) y luego mostró un criterio frágil y una reaparición intermitente de la
> reconstrucción de clases (v1.3). El runner incluye calentamiento del modelo y reintentos
> ante errores de conexión. Resultado de la corrida del 2026-08-12: 27/28 (único pendiente:
> limitación conocida del Arquitecto Python).

---

## Fase 5 - Reevaluación con modelos de mayor capacidad

- [ ] Reevaluar Arquitecto Python con Qwen 7B o superior (derivación conceptual a Profesor ML).
- [x] Reevaluar Revisor de Código (la reconstrucción de fragmentos pequeños se resolvió en
  v1.2 con el prompt, y en v1.3 se estabilizó para análisis sin bloques de código, sin
  requerir un modelo mayor).