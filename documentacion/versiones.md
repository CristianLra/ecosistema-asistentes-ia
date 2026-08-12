# Versiones del Ecosistema

| Asistente | Versión | Estado |
|-----------|----------|--------|
| Mentor de Proyectos | v1.0 | Estable |
| Arquitecto Python | v1.2 | Estable* |
| Profesor DL | v1.1 | Estable |
| Profesor ML | v1.2 | Estable |
| Revisor de Código | v1.3 | Estable |
| Investigador | v1.4 | Estable |
| Tutor de Matemáticas | v1.1 | Estable |

---

## Convención de versiones

- **v0.x** → Desarrollo inicial.
- **v1.0** → Primera versión estable.
- **v1.1, v1.2...** → Mejoras incrementales.
- **v2.0** → Rediseño importante del asistente.

---

## Notas

- **Arquitecto Python (\*):** tiene una limitación conocida documentada — ante preguntas
  conceptuales directas de Machine Learning/Deep Learning (ej. "¿Qué es el overfitting?"),
  explica el concepto en lugar de derivar al Profesor ML. Se probaron dos correcciones de
  prompt sin éxito; se atribuye al modelo base (Qwen 2.5 Coder 3B). Ver
  `asistentes/arquitecto-python/README.md`.

- **Revisor de Código:** la limitación conocida de v1.0/v1.1 (reconstruir implementaciones
  completas ante fragmentos pequeños) se resolvió en v1.2 mediante reglas en el Modelfile
  (árbol de decisión según la pregunta del usuario), detectadas por la automatización de
  pruebas (Fase 4). En v1.3 se corrigió un criterio frágil de la Prueba 002 (el asistente
  proponía mejoras válidas con otra redacción) y una reaparición intermitente de la
  reconstrucción de la clase vacía en la Prueba 003 (se prohibieron los bloques de código
  cuando solo se pide análisis). Nota: a temperatura 0.0 las respuestas no son 100%
  deterministas; validar con más de una corrida. Ver
  `asistentes/revisor-codigo/changelog.md` y `pruebas.md`.

- **Profesor DL:** el comportamiento anómalo observado anteriormente en Continue fue atribuido a
  la extensión y no al Modelfile. El asistente funciona correctamente al ejecutarse directamente
  con Ollama.

- **Investigador:** no tiene limitación conocida. En preguntas mixtas (comparación de
  tecnologías + solicitud de código en la misma consulta) se detectó el mismo tipo de hueco
  de derivación parcial visto en Profesor ML/DL ("código como ejemplo"), con una variante:
  la primera corrección hizo que derivara la pregunta completa en lugar de responder solo la
  parte de código. Se resolvió en el tercer intento de prompt, separando la respuesta en dos
  pasos obligatorios e independientes (comparación siempre / código solo si se pidió, nunca
  el segundo a costa del primero). A diferencia de Arquitecto Python y Revisor de Código, sí
  se corrigió — pero requirió tres iteraciones en vez de las dos habituales. En v1.4 la
  automatización de pruebas detectó un fallo adicional en la funcionalidad core (rechazaba
  preguntas de comparación y las derivaba al Arquitecto Python), corregido con una regla
  explícita de comparación como rol core. Ver `asistentes/investigador/README.md` y
  `asistentes/investigador/pruebas.md`.

- **Tutor de Matemáticas:** no tiene limitación conocida. En v1.0 falló la derivación de
  conceptos de Deep Learning expresados con regla de la cadena y gradientes (ej. "¿qué es
  backpropagation?") — el Tutor explicaba el concepto completo usando las herramientas
  matemáticas que sí le corresponden. Se corrigió en v1.1 con un ejemplo concreto de
  pregunta/respuesta esperada y el cierre explícito de ese hueco. Queda una observación
  cosmética en preguntas mixtas (menciona "descenso del gradiente" como marco al final del
  paso matemático), sin explicar el algoritmo. Ver
  `asistentes/tutor-matematicas/README.md` y `asistentes/tutor-matematicas/pruebas.md`.

---

## Metodología de reevaluación aplicada (2026-08-04)

Los 5 asistentes fueron revalidados con un proceso consistente:

1. Revisión del Modelfile, especificación y pruebas existentes antes de correr nada.
2. Detección de puntos ciegos (por ejemplo, ausencia de pruebas de derivación) y corrección
   preventiva cuando aplicaba.
3. Ejecución de las preguntas predeterminadas vía `ollama run`.
4. Cuando una prueba fallaba por un problema de derivación entre asistentes, se aplicó
   iterativamente: lenguaje categórico → ejemplo concreto de respuesta → exigencia literal
   verificable (esta última solo fue necesaria una vez, en Revisor de Código).
5. Tras dos intentos fallidos de corregir un mismo punto mediante el prompt, se documentó como
   limitación conocida del modelo base en lugar de seguir iterando indefinidamente.

Ver `documentacion/decisiones.md` para el detalle de esta metodología como decisión formal.
