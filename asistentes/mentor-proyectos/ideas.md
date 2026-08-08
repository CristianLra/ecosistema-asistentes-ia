# Ideas

## Pendientes

- Mejorar la planificación de proyectos grandes.
- Incorporar recomendaciones según el estado del proyecto.
- Ayudar a detectar riesgos antes de que aparezcan.
- Añadir una prueba de derivación al Revisor de Código (aún no existe un ejemplo para este caso).

---

## En evaluación

- Integración con RAG para consultar documentación del proyecto.
- Seguimiento automático del progreso entre conversaciones.
- Plantillas para distintos tipos de proyectos.
- **Consistencia de la priorización entre corridas:** ante entradas similares (mismas 4 tareas a
  priorizar), el asistente propuso órdenes distintos en corridas separadas. Ninguno de los dos
  órdenes es incorrecto, pero conviene vigilar si esto afecta la confianza del usuario en la
  recomendación. Revisar en próximas rondas de pruebas.
- **Generalización de la derivación al Arquitecto Python:** la Prueba 003 valida la respuesta ante
  una única formulación ("Créame una API completa..."). Falta confirmar que el asistente deriva
  igual de bien ante variaciones (ej. "impleméntamela", "necesito el backend completo",
  "hazme el código de la API").
- **Tendencia leve a acercarse a implementación tras derivar:** después de derivar correctamente
  al Arquitecto Python, el asistente mencionó instalación de dependencias
  (`pip install fastapi uvicorn`) y "configurar un proyecto FastAPI básico". No llegó a escribir
  código, pero es una señal a vigilar — podría escalar a una implementación real en otras
  variantes de la pregunta.

---

## Implementadas

- Primera versión del Mentor de Proyectos.
- Organización de proyectos por etapas.
- Priorización de tareas.
- Recomendación del siguiente paso.
- Integración con el ecosistema de asistentes.
- Migración de modelo base de Qwen2.5-Coder 3B a Gemma 3 4B, alineado con el criterio de
  `decisiones.md` (Gemma para asistentes consultivos/educativos).
- Refuerzo de la regla de derivación al Arquitecto Python mediante lenguaje categórico y un
  ejemplo concreto de respuesta, tras detectar que la instrucción original no era suficiente.
