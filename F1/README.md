# Fase 1 — Definición y entorno reproducible

Implementación inicial del entorno reproducible del proyecto, dentro del marco
del ABP de Ciencia de Datos Reproducible (MCDI500 — UNAB).

## Contenido
- `notebooks/F1_Definicion.ipynb`: definición del problema, objetivos, validación del entorno y vinculación con el mapa conceptual técnico.
- `src/f1_utils.py`: funciones de captura y validación del entorno (modularidad).
- `docs/`: documentación técnica de la fase.

## Evidencias de rúbrica F1
- Estructura reproducible del repositorio.
- Entorno virtual (`.venv`) y `requirements.txt`.
- Notebook ejecutable `notebooks/F1_Definicion.ipynb`.
- Módulo `src/f1_utils.py` con funciones base.
- Documentación técnica en `docs/`.
- Git/GitHub con commits descriptivos.
- Vinculación con el mapa conceptual técnico.

## Ejecución
Desde la raíz del repositorio, con el entorno virtual activado:

```bash
# macOS / Linux
source .venv/bin/activate
jupyter lab F1/notebooks/F1_Definicion.ipynb
```

```powershell
# Windows
.\.venv\Scripts\Activate.ps1
jupyter lab F1\notebooks\F1_Definicion.ipynb
```

Ejecutar todas las celdas (Restart & Run All). No debe producir errores.

## Dependencias
pandas, numpy, jupyter y utilidades de notebook (ver `requirements.txt`).
