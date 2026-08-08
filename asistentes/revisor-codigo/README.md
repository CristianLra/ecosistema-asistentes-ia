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

Versión estable (v1.1), con una limitación conocida documentada.

---

## Limitaciones conocidas

- Ante fragmentos pequeños de código con poca o ninguna funcionalidad (por ejemplo, una clase
  vacía), el asistente detecta correctamente los problemas de mantenibilidad, pero tiende a
  generar una implementación completa del fragmento en lugar de limitarse a analizarlo, a pesar
  de que el Modelfile lo indica explícitamente.
- Esta limitación se evaluó dos veces (v1.0 y v1.1) sin cambios en el resultado, lo que sugiere
  que proviene del modelo base (Qwen 2.5 Coder 3B) — afinado para completar código — más que del
  prompt.
- Se volverá a evaluar cuando se migre a un modelo de mayor capacidad (7B o superior).

Ver `pruebas.md` (Prueba 003) para el detalle.

---

## Estructura

Este asistente contiene:

- README.md
- Modelfile
- especificacion.md
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

2026-08-06
