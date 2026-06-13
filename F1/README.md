# Fase 1 — Definición y entorno reproducible

Implementación inicial del entorno reproducible del proyecto, dentro del marco
del ABP de Ciencia de Datos Reproducible (MCDI500 — UNAB).

## Contenido

- `notebooks/F1_Definicion.ipynb`: definición del problema, objetivos, validación del entorno y vinculación con el mapa conceptual técnico.
- `src/f1_utils.py`: funciones de captura y validación del entorno (modularidad).
- `docs/`: documentación técnica de la fase, incluye `informe_sumativa1_Final.md` y el PDF de la sumativa.
- `data/`: estructura de datos crudos y procesados de la fase.

## Evidencias de rúbrica F1

- Estructura reproducible del repositorio.
- Entorno virtual (`.venv`) y `requirements.txt` (el entorno se excluye del control de versiones vía `.gitignore`).
- Notebook ejecutable `notebooks/F1_Definicion.ipynb`.
- Módulo `src/f1_utils.py` con funciones base.
- Documentación técnica en `docs/`.
- Git/GitHub con commits descriptivos e identificables por integrante.
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

## Contribución del equipo en la Fase 1

La participación se evidencia mediante los commits individuales registrados en el
historial de Git (identidades consolidadas vía `.mailmap`; ver README principal).

| Integrante | Commits en F1 | Participación |
|---|---|---|
| Rodrigo Chinchón Ayala | 22 | 59% |
| Pablo Villalobos González | 12 | 32% |
| Sergio Fernández Almonacid | 3 | 8% |
| **Total** | **37** | **100%** |

Aportes principales por integrante:

- **Rodrigo Chinchón Ayala**: estructura del repositorio, configuración del entorno reproducible, notebook de definición y módulo `f1_utils.py`.
- **Pablo Villalobos González**: documentación técnica de la fase y desarrollo de la definición del problema.
- **Sergio Fernández Almonacid**: revisión metodológica y validación de la trazabilidad técnica.
