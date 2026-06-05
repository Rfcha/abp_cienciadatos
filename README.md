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
