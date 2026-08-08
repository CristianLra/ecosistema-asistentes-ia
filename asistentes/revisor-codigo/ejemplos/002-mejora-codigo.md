# Ejemplo 002 - Mejora de código

## Objetivo

Comprobar que el asistente propone mejoras puntuales sin cambiar el objetivo del código.

---

## Entrada

```text
¿Cómo mejorarías este código?

x = []

for i in range(100):
    x.append(i)
```

---

## Resultado esperado

- Detecta al menos una mejora válida.
- Explica brevemente por qué la mejora es conveniente.
- Mantiene el mismo comportamiento del código.
- No reescribe más código del necesario.

---

## Criterios de calidad

- Prioriza mejoras simples y justificadas.
- Evita cambios innecesarios.
- No modifica el objetivo del código.
- Mantiene un enfoque de revisión, no de reescritura.

---

## Notas

Una solución como una comprensión de listas (`[i for i in range(100)]`) es una mejora válida, pero no debe presentar una implementación completamente diferente si no aporta un beneficio claro.