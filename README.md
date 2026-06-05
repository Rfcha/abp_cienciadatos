<<<<<<< HEAD
# Proyecto ABP — Ciencia de Datos Reproducible (MCDI500)

Repositorio del proyecto transversal. Grupo 3.

## Integrantes
- Rodrigo Chinchón Ayala
- Sergio Fernández Almonacid
- Pablo Villalobos González

## Estructura

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── F1/                         Fase 1 — Definición y entorno reproducible
│   ├── notebooks/F1_Definicion.ipynb
│   └── src/f1_utils.py
└── F2/                         Fase 2 — Obtención, limpieza y transformación
    ├── notebooks/F2_Preprocesamiento.ipynb
    ├── src/preprocessing.py
    └── data/
        ├── raw/dataset_base.csv
        └── processed/           (se genera al ejecutar el pipeline)
```

## Entorno reproducible

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución
- Fase 1: abrir `F1/notebooks/F1_Definicion.ipynb` y ejecutar todas las celdas.
- Fase 2: abrir `F2/notebooks/F2_Preprocesamiento.ipynb` y ejecutar todas las celdas.

Ambos notebooks se ejecutan sin errores en el entorno descrito.
=======
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
>>>>>>> 10a630b32eaf59ab6dc8927cdba17bbf7caf4d8b
