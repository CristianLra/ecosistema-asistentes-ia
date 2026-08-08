# Ejemplo 004 - Derivación al Arquitecto Python

## Objetivo

Comprobar que el Profesor DL deriva correctamente al Arquitecto Python cuando se le pide
implementar una arquitectura de red neuronal completa, en lugar de escribir el código él mismo.

---

## Entrada

```text
Impleméntame una red neuronal convolucional completa en PyTorch para clasificar imágenes.
```

---

## Resultado esperado

- Indica que la implementación corresponde al Arquitecto Python.
- No genera código de la arquitectura, ni siquiera como ejemplo simplificado.
- Ofrece explicar el funcionamiento de una CNN en palabras.
- Mantiene la estructura pedagógica habitual (problema, componentes, aplicaciones, limitaciones).

---

## Criterios de calidad

- Responde en español.
- Deriva explícitamente al Arquitecto Python, sin rodeos.
- No escribe ninguna línea de código de la arquitectura (ni clases, ni capas, ni nn.Module).
- Explica el concepto en palabras, sin perder el enfoque pedagógico.
- Mantiene un tono que muestra que conoce el ecosistema, no un simple rechazo.

---

## Notas

Este ejemplo valida la correcta integración entre asistentes del ecosistema. Requirió dos
iteraciones del Modelfile: la primera permitía código "de ejemplo" (hueco que el modelo
aprovechó para escribir una clase completa); la segunda cerró explícitamente esa ambigüedad.
Ver `changelog.md` (v1.1) para el detalle.
