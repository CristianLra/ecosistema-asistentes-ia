# Ejemplo 003 - Problemas de mantenibilidad

## Objetivo

Comprobar que el asistente detecta problemas de mantenibilidad sin generar una implementación completa cuando no es necesaria.

---

## Entrada

```text
¿Qué problemas de mantenibilidad tiene este código?

class Usuario:

    pass
```

---

## Resultado esperado

- Detecta la falta de funcionalidad de la clase.
- Explica los posibles problemas de mantenibilidad.
- No inventa funcionalidades que el usuario no ha solicitado.
- Evita generar una implementación completa.

---

## Criterios de calidad

- Prioriza el análisis sobre la implementación.
- Justifica brevemente cada observación.
- Mantiene el enfoque de revisión de código.

---

## Notas

Debe limitarse a revisar el fragmento proporcionado.