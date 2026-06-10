# Fase 2 — Obtención, limpieza y transformación de datos

Pipeline reproducible de preprocesamiento de datos, dentro del marco del ABP de
Ciencia de Datos Reproducible (MCDI500 — UNAB).

## Contenido

- `notebooks/F2_Preprocesamiento.ipynb`: orquestación y documentación del pipeline.
- `src/preprocessing.py`: funciones del pipeline (load, profile, clean, transform, validate, run_pipeline).
- `data/raw/dataset_base.csv`: dataset crudo con defectos deliberados (nulos, duplicados, texto inconsistente).
- `data/processed/dataset_procesado.csv`: dataset procesado (se genera al ejecutar el pipeline).
- `docs/`: documentación de la fase, incluye `aporte_metodologico_f2_SFA.md` y el informe de la sumativa.

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

## Contribución del equipo en la Fase 2

La participación se evidencia mediante los commits individuales registrados en el
historial de Git (identidades consolidadas vía `.mailmap`; ver README principal).

| Integrante | Commits en F2 | Participación |
|---|---|---|
| Rodrigo Chinchón Ayala | 19 | 66% |
| Sergio Fernández Almonacid | 8 | 28% |
| Pablo Villalobos González | 2 | 7% |
| **Total** | **29** | **100%** |

Aportes principales por integrante:

- **Rodrigo Chinchón Ayala**: diseño y orquestación del pipeline, módulo `preprocessing.py`, notebook de preprocesamiento y validación técnica.
- **Sergio Fernández Almonacid**: aporte metodológico (`aporte_metodologico_f2_SFA.md`) y revisión de la limpieza y transformación de datos.
- **Pablo Villalobos González**: apoyo en la exploración inicial y documentación del dataset.
