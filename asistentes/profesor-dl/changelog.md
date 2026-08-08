# Changelog

Registro de cambios del Profesor DL.

---

## v1.0

### Fecha

2026-08-03

### Cambios

- Primera versión del Profesor DL.
- Especializado en Deep Learning.
- Explicaciones progresivas.
- Prioriza la comprensión antes que el código.
- Integración con el ecosistema de asistentes.

---

## v1.1

### Fecha

2026-08-04

### Cambios

- Se detectó que el Modelfile no tenía ninguna sección de límites, pese a que la especificación
  ya indicaba que no debía sustituir al Arquitecto Python ni desarrollar proyectos completos. Se
  agregó dicha sección.
- Primer intento: regla de "no generar implementaciones completas" con ejemplo de derivación.
  Resultado parcial — el modelo derivaba en el discurso pero igual escribía código etiquetado
  como "ejemplo simplificado".
- Segundo intento: se cerró la ambigüedad especificando que no debe escribirse ninguna línea de
  código de la arquitectura, sin importar cómo se justifique. Este ajuste sí funcionó.
- Se añadió la Prueba 004 (derivación al Arquitecto Python), ahora aprobada.
- Se creó el ejemplo `ejemplos/004-derivacion-arquitecto-python.md`, que no existía antes.

---

## Próxima versión

### Mejoras previstas

- Mejorar las analogías.
- Añadir más ejemplos.
- Evaluar integración mediante RAG.
- Confirmar que la derivación al Arquitecto Python generaliza ante otras formas de pedir
  implementación (no solo CNN, también RNN, Transformers, etc.).
