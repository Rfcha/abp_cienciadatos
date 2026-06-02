# Proyecto ABP - Ciencia de Datos Reproducible

**Curso:** Programacion para la Ciencia (202681.2535)  
**Docente:** Dr. Omar Salinas Silva  
**Equipo:**
- Rodrigo Chinchon
- Pablo Villalobos
- Sergio Fernandez

## Problematica
COMPLETAR: definir la problematica asignada al equipo, el contexto, la necesidad tecnica y el valor analitico del proyecto.

## Objetivo general
COMPLETAR: construir un flujo reproducible de obtencion, limpieza y transformacion de datos utilizando Python, Jupyter, Pandas, NumPy y GitHub.

## Estructura del repositorio

``text
F1/                 # Sumativa 1: definicion, entorno reproducible y documentacion
F2/                 # Sumativa 2: notebook de obtencion, limpieza y transformacion
common/             # utilidades comunes
requirements.txt    # dependencias reproducibles
logs/               # bitacoras locales de setup
``

## Reproducibilidad

``powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name abp_ds_ai --display-name "Python (abp_ds_ai)"
jupyter lab
``

## Flujo Git recomendado

``bash
git status
git add .
git commit -m "docs: completa definicion tecnica F1"
git commit -m "feat: implementa pipeline inicial F2"
git push
``

## Entregables

- **F1:** informe PDF, notebook F1/notebooks/F1_Definicion.ipynb, README F1, evidencia de entorno y repositorio GitHub.
- **F2:** informe PDF, notebook F2/notebooks/F2_Preprocesamiento.ipynb, dataset procesado, README F2, evidencias de validacion y repositorio actualizado.