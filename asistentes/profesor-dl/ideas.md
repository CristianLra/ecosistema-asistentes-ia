# Ideas

## Pendientes

- Mejorar las analogías utilizadas en algunos conceptos.
- Crear más ejemplos de redes neuronales.
- Añadir ejemplos sobre CNN, RNN y Transformers.
- Validar que la derivación al Arquitecto Python generaliza ante otras arquitecturas (RNN,
  Transformers) y otras formas de pedirlo.

---

## En evaluación

- Integrar ejemplos mediante RAG.
- Adaptar automáticamente la profundidad según el progreso del estudiante.

---

## Implementadas

- Primera versión del Profesor DL.
- Explicaciones progresivas.
- Relación entre Machine Learning y Deep Learning.
- Sección de límites en el Modelfile (no existía en v1.0).
- Derivación correcta al Arquitecto Python ante solicitudes de implementación completa.

---

## Aprendizajes para el ecosistema

- Cuando una regla de "no generes X" deja margen a interpretaciones ("completo" vs "de
  ejemplo"/"simplificado"), el modelo puede aprovechar ese margen aunque reconozca la regla
  en el discurso. Cerrar explícitamente todas las variantes de la ambigüedad (no solo decir
  "no generes el proyecto completo", sino "no generes ninguna línea de código de X") resolvió
  el problema aquí. Vale la pena revisar si esta misma técnica ayuda en otros asistentes con
  reglas de derivación pendientes.
