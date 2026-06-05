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
