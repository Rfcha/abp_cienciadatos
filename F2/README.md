# Fase 2 - Notebook de obtencion, limpieza y transformacion de datos

## Proposito
Implementar un pipeline inicial y reproducible de obtencion, limpieza, depuracion, transformacion y validacion de datos usando Python, NumPy, Pandas y scikit-learn.

## Dataset
Archivo base: data/raw/dataset_base.csv  
Archivo procesado esperado: data/processed/dataset_procesado.csv

> Reemplazar el dataset demo por el dataset definitivo del grupo si corresponde. Debe contener variables numericas y categoricas.

## Pipeline tecnico

1. Obtencion/carga de datos.
2. Perfilamiento inicial: tipos, nulos, duplicados, cardinalidad.
3. Limpieza: duplicados, nulos, casting y consistencia.
4. Transformacion: normalizacion de variables numericas y encoding de categoricas.
5. Validacion: integridad, ausencia de nulos, duplicados y salida final trazable.

## Ejecucion

``powershell
cd "D:\LM_IA_LAB\04_PROJECTS\abp_cienciadatos"
.\.venv\Scripts\Activate.ps1
jupyter lab F2\notebooks\F2_Preprocesamiento.ipynb
``