# Observaciones técnicas y de análisis - Fase 3

## 1. Propósito del documento

Este documento registra observaciones técnicas y de análisis sobre la Fase 3 del proyecto, enfocada en el análisis de calidad del aire en Santiago.

## 2. Alcance de la revisión

Las observaciones se orientan principalmente a:

- La comprensión del notebook de exploración.
- La trazabilidad entre datos crudos, limpieza y análisis.
- La revisión de valores nulos y registros relevantes.
- La interpretación de resultados y visualizaciones.
- La claridad de las conclusiones que se desprenden de los datos.

## 3. Observaciones técnicas

| Aspecto revisado | Observación | Recomendación |
|---|---|---|
| Carga de datos | Es importante que la ruta, separador, decimal y codificación del archivo estén claramente documentados. | Mantener una breve explicación del formato de carga utilizado. |
| Valores nulos | La revisión de nulos es clave para evaluar la calidad del dataset. | Indicar no solo el total de nulos, sino también su porcentaje respecto del dataset. |
| Variable objetivo | La eliminación de registros sin medición de MP2.5 debe quedar claramente justificada. | Explicar por qué MP2.5 se considera una variable relevante para el análisis. |
| Dataset limpio | Es positivo guardar una versión procesada del dataset. | Asegurar que se mantenga diferenciada de los datos crudos. |
| Reproducibilidad | El notebook debe permitir comprender el flujo desde carga hasta análisis. | Agregar comentarios breves en celdas clave para facilitar la lectura. |

## 4. Observaciones de análisis

| Aspecto revisado | Observación | Recomendación |
|---|---|---|
| Interpretación de resultados | Los resultados deben distinguir entre descripción de datos e interpretación. | Separar claramente hallazgos observados de posibles explicaciones. |
| Visualizaciones | Los gráficos deben permitir entender variable, periodo y unidad de medida. | Revisar títulos, ejes, leyendas y notas explicativas. |
| Tendencias | Si se identifican patrones temporales, deben sustentarse con el periodo observado. | Evitar hablar de tendencia si el periodo es limitado o presenta datos faltantes. |
| Comparaciones | Las comparaciones deben considerar misma unidad, periodo y criterio. | Declarar si se comparan promedios, máximos u otras métricas. |
| Conclusiones | Las conclusiones deben derivarse directamente de los datos analizados. | Evitar afirmaciones causales si el análisis es exploratorio. |


## 5. Preguntas de apoyo para el equipo

Para fortalecer la revisión analítica del proyecto, se proponen las siguientes preguntas:

- ¿Qué periodo cubren los datos analizados?
- ¿Qué contaminantes o variables ambientales son más relevantes?
- ¿Por qué se selecciona MP2.5 como variable principal?
- ¿Cuántos registros se eliminan durante la limpieza?
- ¿El dataset procesado conserva información suficiente para analizar patrones?
- ¿Las visualizaciones muestran claramente unidades, periodo y fuente?
- ¿Las conclusiones están alineadas con los resultados observados?
- ¿Qué limitaciones deben declararse antes de presentar los hallazgos?

## 7. Recomendaciones generales

Se recomienda que la Fase 3 refuerce la conexión entre:

1. El problema ambiental analizado.
2. Los datos disponibles.
3. Las decisiones de limpieza.
4. Las visualizaciones generadas.
5. Las conclusiones finales.

Esta conexión permite que el análisis no sea solo técnico, sino también comprensible, trazable y útil para comunicar resultados a una audiencia más amplia.

## 8. Aporte al proyecto

La contribución busca fortalecer el proyecto desde una mirada crítica, metodológica y orientada a la comprensión del análisis de datos.