# Fase 2 — Obtención, limpieza y transformación de datos

Pipeline reproducible de preprocesamiento de datos, dentro del marco del ABP de
Ciencia de Datos Reproducible (MCDI500 — UNAB).

## Contenido
- `notebooks/F2_Preprocesamiento.ipynb`: orquestación y documentación del pipeline.
- `src/preprocessing.py`: funciones del pipeline (load, profile, clean, transform, validate, run_pipeline).
- `data/raw/dataset_base.csv`: dataset crudo con defectos deliberados (nulos, duplicados, texto inconsistente).
- `data/processed/`: dataset procesado (se genera al ejecutar el pipeline).

## Pipeline técnico
1. Obtención y exploración inicial (perfilado de tipos, nulos, duplicados y cardinalidad).
2. Limpieza: eliminación de duplicados, casting, imputación con mediana, normalización textual.
3. Transformación: normalización MinMax de variables numéricas y One Hot Encoding de categóricas.
4. Validación técnica: casos normales, límite y excepciones; ausencia de nulos y duplicados; salida trazable.
5. Persistencia del dataset procesado en `data/processed/dataset_procesado.csv`.

## Ejecución
Desde la raíz del repositorio, con el entorno virtual activado:

```bash
# macOS / Linux
source .venv/bin/activate
jupyter lab F2/notebooks/F2_Preprocesamiento.ipynb
```

```powershell
# Windows
.\.venv\Scripts\Activate.ps1
jupyter lab F2\notebooks\F2_Preprocesamiento.ipynb
```

Ejecutar todas las celdas (Restart & Run All). No debe producir errores.

## Dependencias
numpy, pandas, scikit-learn, jupyter y utilidades de notebook (ver `requirements.txt`).
