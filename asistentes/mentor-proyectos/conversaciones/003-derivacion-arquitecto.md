# Conversación de validación 001

## Asistente

Mentor de Proyectos

---

## Fecha

2026-08-04

---

## Versión

v1.0

---

## Objetivo

Validar que el asistente deriva correctamente al Arquitecto Python cuando se le solicita
generar una implementación completa, tras el ajuste del prompt (regla categórica + ejemplo
concreto de respuesta).

---

# Conversación

## Usuario

```text
Créame una API completa con FastAPI para este proyecto.
```

---

## Asistente

```text
Esa implementación le corresponde al Arquitecto Python, él puede construirla siguiendo buenas
prácticas de arquitectura. Yo puedo ayudarte a definir qué endpoints necesita tu API y en qué
momento del proyecto conviene construirla. ¿Quieres que lo veamos desde ese ángulo?

Para ayudarte a definir los requisitos de la API, vamos a estructurarla por fases. Voy a pedirte
que me digas:

1. ¿Qué tipo de predicciones necesitas obtener con la API? Por ejemplo, solo el precio estimado o
también información adicional como la confianza en la predicción?
2. ¿Qué características (variables) vas a incluir en tus predicciones? (Ejemplo: tamaño de la
vivienda, número de habitaciones, ubicación, etc.)
3. ¿Cómo quieres que se formatee la respuesta de la API? (Ejemplo: JSON con el precio y una
puntuación de confianza, o un formato personalizado)

Una vez que tengamos estos detalles, podemos definir los endpoints de la API, por ejemplo:

- /predict: Recibe los datos de la vivienda como entrada y devuelve la predicción del precio.
- /health: (Opcional) Verifica si la API está funcionando correctamente.

Mientras tanto, vamos a configurar un proyecto FastAPI básico. Necesitaremos instalar las
dependencias necesarias:

pip install fastapi uvicorn

Uvicorn es un servidor ASGI que se utiliza para ejecutar aplicaciones FastAPI. Después de instalar
estas dependencias, podemos crear la estructura básica de tu API.

¿Qué te parece si comenzamos definiendo estos requisitos antes de pasar a la implementación?
```

---

## Observaciones

- ✅ Derivó correctamente al Arquitecto Python en la primera línea, sin generar código.
- ✅ No implementó la API ni escribió código de implementación.
- ✅ Explicó el motivo y ofreció seguir ayudando desde su rol (definir endpoints, requisitos).
- ⚠️ Tras derivar, se acercó a terreno de implementación al mencionar la instalación de
  dependencias (`pip install fastapi uvicorn`) y "configurar un proyecto FastAPI básico". No llegó
  a escribir código, pero es una señal a vigilar en próximas validaciones.
- ⚠️ Esta prueba valida la respuesta ante una única formulación de la solicitud ("Créame una API
  completa..."). Falta confirmar que la derivación generaliza ante variaciones (ej. "impleméntamela",
  "necesito el backend completo").

---

## Conclusión

Aprobada. Ver `ideas.md` (sección "En evaluación") para los puntos de seguimiento pendientes.
