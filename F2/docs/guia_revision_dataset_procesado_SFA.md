# Guía de revisión del dataset procesado - Fase 2

## 1. Propósito del documento

Este documento tiene como propósito aportar una guía simple para revisar si el dataset procesado de la Fase 2 se encuentra en condiciones adecuadas para ser utilizado en las siguientes etapas del proyecto.

La revisión esta orientada a fortalecer la calidad, trazabilidad y comprensión del proceso de preparación de datos sin ser experto en programación.

## 2. Importancia de revisar el dataset procesado

En un proyecto de ciencia de datos, el dataset procesado constituye la base para el análisis exploratorio, la generación de visualizaciones y el eventual uso de modelos.

Es necesario revisar si el resultado final es comprensible, consistente y coherente con el problema que se busca analizar.

## 3. Aspectos mínimos a verificar

| Aspecto | Pregunta orientadora | Observación |
|---|---|---|
| Existencia del archivo | ¿El dataset procesado fue generado correctamente? | Confirmar que el archivo existe en la carpeta esperada. |
| Diferencia con datos crudos | ¿Se distingue claramente del dataset original? | Revisar que no se sobrescriban los datos originales. |
| Columnas disponibles | ¿Las columnas finales son comprensibles? | Identificar variables eliminadas, transformadas o creadas. |
| Valores nulos | ¿Persisten datos faltantes relevantes? | Evaluar si los nulos restantes afectan el análisis. |
| Duplicados | ¿Existen registros duplicados? | Confirmar si fueron eliminados o justificados. |
| Tipos de datos | ¿Los tipos de datos son coherentes? | Revisar fechas, números, textos y categorías. |
| Interpretabilidad | ¿Las variables siguen siendo entendibles? | Evitar transformaciones que oculten el significado de los datos. |

## 4. Preguntas para validar la calidad del resultado

- ¿El dataset final mantiene relación con el problema definido?
- ¿Se eliminaron columnas necesarias para el análisis posterior?
- ¿Las transformaciones aplicadas están documentadas?
- ¿El archivo procesado puede ser explicado por un integrante no técnico?
- ¿Existe una versión original disponible para comparación?
- ¿Las decisiones de limpieza fueron justificadas?
- ¿El dataset está listo para análisis exploratorio o requiere una nueva revisión?

## 5. Riesgos asociados al uso del dataset procesado

- Trabajar con un archivo incompleto o mal generado.
- Perder trazabilidad entre datos crudos y datos transformados.
- Usar variables codificadas sin comprender su significado.
- Eliminar datos relevantes durante la limpieza.
- No registrar supuestos utilizados en el preprocesamiento.
- Confundir un dataset técnicamente válido con uno analíticamente útil.

## 6. Recomendación antes de avanzar

Antes de pasar a una nueva fase del proyecto, se recomienda que el equipo revise en conjunto:

1. Qué archivo corresponde al dataset procesado.
2. Qué transformaciones principales se aplicaron.
3. Qué columnas fueron eliminadas o creadas.
4. Qué limitaciones permanecen.
5. Qué uso tendrá el dataset en la siguiente etapa.

## 7. Aporte al proyecto

Esta guía busca fortalecer la revisión del dataset procesado desde una mirada complementaria a la programación.

Su aporte consiste en promover una revisión más consciente del resultado final de la Fase 2, conectando el trabajo técnico de limpieza y transformación con la utilidad posterior del análisis.