<<<<<<< HEAD
# Fase 2 — Obtención, limpieza y transformación de datos

Pipeline reproducible de preprocesamiento sobre un dataset de cartera de clientes.

## Contenido
- `notebooks/F2_Preprocesamiento.ipynb`: orquestación y documentación del pipeline.
- `src/preprocessing.py`: funciones del pipeline (load, profile, clean, transform, validate, run_pipeline).
- `data/raw/dataset_base.csv`: dataset crudo con defectos deliberados (nulos, duplicados, texto inconsistente).
- `data/processed/`: dataset procesado (se genera al ejecutar).

## Ejecución
Desde la raíz del repositorio, con el entorno activado:
```bash
jupyter notebook F2/notebooks/F2_Preprocesamiento.ipynb
```
Ejecutar todas las celdas (Restart & Run All). No produce errores.

## Pipeline
1. Obtención y exploración inicial (perfilado de nulos/duplicados).
2. Limpieza: duplicados, casting, imputación con mediana, normalización textual.
3. Transformación: normalización MinMax + One Hot Encoding.
4. Validación técnica: casos normales, límite y excepciones.
5. Persistencia del dataset procesado.
=======
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
>>>>>>> 10a630b32eaf59ab6dc8927cdba17bbf7caf4d8b
