# Ideas

## Pendientes

- Incorporar más ejercicios prácticos de Machine Learning.
- Crear rutas de aprendizaje por niveles.
- Añadir más ejemplos utilizando datasets reales.
- Mejorar las analogías para conceptos complejos.
- Validar que la derivación al Arquitecto Python generaliza ante otros algoritmos y formas de
  pedir implementación.

---

## En evaluación

- Adaptar automáticamente la profundidad según el nivel del estudiante.
- Integrar ejemplos mediante RAG.
- Generar cuestionarios de autoevaluación.

---

## Implementadas

- Primera versión del Profesor ML.
- Explicaciones paso a paso.
- Enseñanza orientada a la comprensión.
- Separación clara respecto a Profesor DL y Arquitecto Python.
- Derivación correcta al Arquitecto Python ante solicitudes de implementación completa, incluso
  en formato de guía paso a paso.

---

## Aprendizajes para el ecosistema

- Confirmado con un segundo caso (después de Profesor DL): cuando una regla de derivación deja
  margen a reformular la respuesta bajo una etiqueta distinta ("ejemplo", "guía paso a paso",
  "esqueleto básico"), el modelo puede aprovechar ese margen aunque reconozca la regla en el
  discurso. La solución efectiva en ambos casos fue nombrar explícitamente cada variante posible
  del hueco, no solo la más obvia.
