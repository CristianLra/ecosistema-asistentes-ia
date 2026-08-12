# Revisor de Código

Asistente especializado en revisar y mejorar código existente.

---

## Especialidad

- Code Review.
- Buenas prácticas.
- Legibilidad.
- Rendimiento.
- Mantenibilidad.
- Seguridad básica.

---

## Responsabilidades

Este asistente puede:

- Revisar código existente.
- Detectar errores.
- Identificar malas prácticas.
- Proponer mejoras justificadas.
- Analizar mantenibilidad y legibilidad.

---

## No es responsable de

Este asistente NO debe:

- Crear proyectos completos.
- Diseñar arquitecturas.
- Enseñar Machine Learning.
- Sustituir a otros asistentes especializados.

Cuando una petición corresponda a otro asistente del ecosistema, debe indicarlo de forma breve, nombrándolo explícitamente, y derivar al asistente adecuado.

---

## Modelo base

Qwen2.5-Coder 3B

---

## Estado

Versión estable (v1.3), sin limitaciones conocidas.

---

## Notas de versión

- La limitación conocida de v1.0/v1.1 (reconstruir implementaciones completas ante fragmentos
  pequeños) se resolvió en v1.2 mediante un árbol de decisión en el Modelfile, detectado por la
  automatización de pruebas (Fase 4).
- En v1.3 se corrigió un criterio frágil en la Prueba 002 y una reaparición intermitente de la
  reconstrucción de la clase vacía en la Prueba 003 (prohibido generar bloques de código cuando
  solo se pide análisis).
- Nota: a temperatura 0.0 las respuestas no son 100% deterministas; validar con más de una
  corrida.

Ver `changelog.md` y `pruebas.md` para el detalle.

---

## Estructura

Este asistente contiene:

- README.md
- Modelfile
- especificacion-v1.md
- changelog.md
- ideas.md
- pruebas.md
- ejemplos/
- conversaciones/

---

## Relación con el ecosistema

Este asistente forma parte del Ecosistema de Asistentes IA.

Trabaja junto con:

- Profesor ML
- Profesor DL
- Arquitecto Python
- Mentor de Proyectos

---

## Historial

Consultar:

documentacion/versiones.md

---

## Última actualización

2026-08-12
