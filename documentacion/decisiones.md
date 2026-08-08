# Decisiones de Arquitectura

## 2026-08-03

### Gemma 3 4B para asistentes educativos

**Decisión**

Utilizar Gemma 3 4B como modelo principal para asistentes orientados a la enseñanza.

**Motivo**

Sigue mejor las instrucciones y mantiene una personalidad más consistente.

---

## 2026-08-03

### Qwen 2.5 Coder para programación

**Decisión**

Utilizar Qwen 2.5 Coder para asistentes centrados en desarrollo de software.

**Motivo**

Genera mejor código y soluciones técnicas.

---

## 2026-08-03

### Un asistente, una responsabilidad

**Decisión**

Cada asistente tendrá una única especialidad.

**Motivo**

Evitar asistentes generalistas y facilitar su mantenimiento.

---

## 2026-08-03

### Documentar antes de modificar

**Decisión**

Toda mejora importante debe reflejarse en la especificación, el changelog y las pruebas.

**Motivo**

Mantener el proyecto versionado y fácil de evolucionar.

## 2026-08-03

### Validación de asistentes

La validación oficial de un asistente se realizará mediante `ollama run`.

Continue se utilizará como interfaz de trabajo, pero sus respuestas no serán el criterio principal para evaluar el comportamiento del asistente, ya que puede añadir contexto o instrucciones adicionales.

### Comportamiento de Continue

Se observó que Continue 2.0 puede modificar parcialmente el comportamiento de los asistentes locales, especialmente en modelos orientados a enseñanza.

Hasta comprender completamente este comportamiento, la validación oficial de los asistentes se realizará mediante `ollama run`.

## 2026-08-06

### Metodología para reglas de derivación entre asistentes

**Decisión**

Cuando un asistente no respeta una regla de derivación hacia otro asistente del ecosistema,
aplicar las siguientes correcciones en orden, deteniéndose en la primera que funcione:

1. Lenguaje categórico ("nunca", "sin excepciones") en lugar de instrucciones suaves ("evita",
   "procura").
2. Un ejemplo concreto de la pregunta del usuario y la respuesta esperada, incluyendo el nombre
   exacto del asistente al que se debe derivar.
3. Cerrar explícitamente los "huecos" que el modelo pueda usar para technically cumplir la regla
   sin respetar su espíritu (por ejemplo, "ejemplo simplificado", "guía paso a paso",
   herramientas externas en lugar del asistente correcto).
4. Si ninguna de las anteriores funciona, exigir que la respuesta incluya literalmente ciertas
   palabras (por ejemplo, el nombre del asistente correcto), de forma verificable.

Si tras dos intentos con enfoques distintos la falla persiste sin cambios, documentar como
limitación conocida del modelo base en el README del asistente, en lugar de seguir iterando el
prompt indefinidamente.

**Motivo**

Se probó sistemáticamente en los 5 asistentes del ecosistema (2026-08-04). En 3 de 5 casos
(Mentor de Proyectos, Profesor DL, Profesor ML) el problema se resolvió con los pasos 1-3. En
Revisor de Código fue necesario llegar al paso 4. En Arquitecto Python, ninguno de los pasos
funcionó tras dos intentos, lo que se interpretó como evidencia de que el problema provenía del
modelo base (Qwen 2.5 Coder 3B) y no del prompt.
