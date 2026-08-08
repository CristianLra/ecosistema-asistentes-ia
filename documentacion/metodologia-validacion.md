# Metodología de Validación

## Objetivo

Garantizar que todos los asistentes del ecosistema se comporten de acuerdo con su especialidad y mantengan un comportamiento consistente a lo largo del tiempo.

---

# Flujo de validación

Todo asistente debe seguir este proceso:

1. Diseñar la especificación.
2. Crear el Modelfile.
3. Construir el modelo con `ollama create`.
4. Validar el comportamiento mediante `ollama run`.
5. Registrar los resultados en `pruebas.md`.
6. Integrar el asistente en Continue.
7. Verificar la integración.
8. Si Continue modifica el comportamiento, considerar la validación oficial la obtenida mediante `ollama run`.

---

# Criterios de aprobación

Cada asistente debe cumplir:

- Mantener su rol.
- Respetar las instrucciones del SYSTEM.
- Responder en el idioma esperado.
- No invadir responsabilidades de otros asistentes.
- Mantener un comportamiento consistente entre distintas conversaciones.

---

# Registro de pruebas

Todas las pruebas deben registrarse en:

- pruebas.md
- changelog.md (cuando exista una mejora)

---

# Revalidación

Un asistente debe volver a evaluarse cuando:

- Se modifique el SYSTEM.
- Cambie el modelo base.
- Se detecte un comportamiento inesperado.
- Se añadan nuevas capacidades.
- Se actualice Ollama o Continue de forma significativa.

---

# Observaciones

Actualmente la validación oficial del comportamiento se realiza mediante `ollama run`.

Continue se considera una interfaz de integración y puede modificar parcialmente el comportamiento del modelo mediante contexto o instrucciones internas.

## Interpretación de resultados

Durante la validación debe distinguirse entre:

- Limitaciones del SYSTEM.
- Limitaciones propias del modelo base.

No todas las desviaciones pueden corregirse únicamente modificando el prompt.