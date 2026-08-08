# Ejemplo 004 - Derivación a concepto de ML

## Objetivo

Verificar que el Investigador deriva preguntas conceptuales de Machine Learning al
Profesor ML, sin repetir el hueco de derivación que persiste en el Arquitecto Python
(limitación conocida: no deriva "¿qué es el overfitting?").

---

## Entrada

​```text
¿Qué es el overfitting?
​```

---

## Resultado esperado

- No explica el concepto, aunque el modelo lo conozca.
- Deriva al Profesor ML, nombrándolo explícitamente.

---

## Criterios de calidad

- Cero explicación conceptual del overfitting.
- Nombra a "Profesor ML" de forma literal.

---

## Notas

Prueba prioritaria: mismo tipo de falla que quedó como limitación conocida en el
Arquitecto Python v1.2. Confirma si el problema es del modelo base (gemma3:4b vs
qwen2.5-coder:3b) o si depende del prompt.