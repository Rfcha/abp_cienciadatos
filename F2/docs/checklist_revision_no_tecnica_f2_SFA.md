# Checklist de revisión no técnica - Fase 2

## 1. Propósito del documento

Este documento tiene como propósito aportar una herramienta simple de revisión para la Fase 2 del proyecto, centrada en la obtención, limpieza y transformación de datos.

El checklist está diseñado desde una perspectiva no experta en programación, pero orientada a fortalecer la comprensión, trazabilidad y calidad del proceso de preprocesamiento de datos.

## 2. Enfoque del aporte

El objetivo es comprender qué cambios se realizan sobre los datos, por qué se realizan y cómo pueden afectar el análisis posterior.

Desde este enfoque, una persona no experta puede contribuir revisando si el proceso es claro, justificable y coherente con los objetivos del proyecto.

## 3. Checklist de revisión general

| Pregunta de revisión | Sí | No | Observaciones |
|---|---|---|---|
| ¿Se identifica claramente el dataset original utilizado? |  |  |  |
| ¿Se distingue entre datos crudos y datos procesados? |  |  |  |
| ¿Se explica qué columnas contiene el dataset? |  |  |  |
| ¿Se identifican valores nulos o faltantes? |  |  |  |
| ¿Se explica cómo se trataron los valores nulos? |  |  |  |
| ¿Se revisa la existencia de registros duplicados? |  |  |  |
| ¿Se justifica la eliminación o conservación de registros? |  |  |  |
| ¿Se revisan los tipos de datos de cada variable? |  |  |  |
| ¿Se documentan las transformaciones aplicadas? |  |  |  |
| ¿Se conserva una versión procesada del dataset? |  |  |  |

## 4. Checklist sobre limpieza de datos

| Aspecto | Pregunta orientadora | Observación sugerida |
|---|---|---|
| Valores nulos | ¿Existen columnas con datos faltantes? | Identificar si los nulos son pocos, muchos o críticos. |
| Duplicados | ¿Hay registros repetidos? | Revisar si son duplicados reales o casos válidos. |
| Formatos | ¿Las fechas, números y textos están en formato correcto? | Verificar consistencia de formatos. |
| Categorías | ¿Una misma categoría aparece escrita de distintas formas? | Ejemplo: mayúsculas, tildes, abreviaciones. |
| Variables irrelevantes | ¿Existen columnas que no aportan al análisis? | Evaluar si deben mantenerse o eliminarse. |
| Valores extremos | ¿Hay datos muy altos o muy bajos que llamen la atención? | No eliminarlos sin justificación previa. |

## 5. Checklist sobre transformación de datos

| Aspecto | Pregunta orientadora | Observación sugerida |
|---|---|---|
| Normalización | ¿Se normalizaron variables numéricas? | Explicar por qué fue necesario. |
| Codificación | ¿Se transformaron variables categóricas? | Revisar si se mantiene la interpretación. |
| Nuevas variables | ¿Se crearon columnas derivadas? | Documentar su fórmula o criterio. |
| Eliminación de columnas | ¿Se eliminaron variables? | Justificar el motivo. |
| Dataset final | ¿El archivo procesado conserva información útil? | Comparar con el dataset original. |

## 6. Riesgos que deben observarse

Durante la revisión no técnica del proceso de limpieza y transformación, se deben considerar algunos riesgos:

- Eliminar datos importantes por error.
- Imputar valores sin justificar el criterio utilizado.
- Transformar variables de manera que pierdan significado.
- Mantener columnas irrelevantes que puedan afectar el análisis.
- No documentar diferencias entre el dataset crudo y el dataset procesado.
- Confundir limpieza de datos con alteración injustificada de la información original.

## 7. Preguntas para el equipo técnico

Para apoyar el trabajo colaborativo, se proponen las siguientes preguntas al equipo técnico:

- ¿Qué cambios principales se hicieron sobre el dataset original?
- ¿Qué columnas fueron eliminadas y por qué?
- ¿Qué valores fueron imputados?
- ¿Qué variables fueron transformadas?
- ¿Qué criterios se usaron para validar el dataset procesado?
- ¿El dataset final está listo para análisis exploratorio o modelamiento?
- ¿Qué limitaciones permanecen después de la limpieza?

## 8. Aporte al proyecto

Este checklist busca apoyar la revisión de la Fase 2 desde una mirada complementaria a la programación. Su utilidad está en facilitar la comprensión del proceso y fortalecer la calidad documental del proyecto.
