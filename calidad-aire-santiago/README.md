# Calidad del aire en Santiago

Proyecto transversal — MCDI500. Análisis de la calidad del aire en Santiago y su
relación con variables meteorológicas, para anticipar episodios críticos de
contaminación por material particulado (MP2.5 / MP10).

## Integrantes (Grupo 3)

- RODRIGO CHINCHÓN AYALA
- SERGIO FERNANDEZ ALMONACID
- PABLO VILLALOBOS GONZALEZ

## Problema

¿Qué condiciones meteorológicas anticipan un episodio crítico de contaminación
por material particulado en Santiago? El proyecto identifica las condiciones
(temperatura, viento, presión, inversión térmica) asociadas a las horas en que
el MP2.5 supera el umbral crítico, para anticipar dichos episodios.

## Datos

Dataset horario de la red **SINCA** (Sistema de Información Nacional de Calidad
del Aire, Ministerio del Medio Ambiente de Chile) para la Región Metropolitana,
periodo 2022-2023.

- **11 estaciones / comunas**: Pudahuel, Cerro Navia, El Bosque, La Florida,
  Puente Alto, Independencia, Quilicura, Cerrillos, Las Condes, Providencia y
  Talagante.
- **192.720 registros** horarios.
- **Variables**:
  - Contaminantes: MP2.5, MP10
  - Meteorológicas: temperatura, humedad, presión, viento, radiación solar,
    inversión térmica
  - Temporales: día de la semana, fin de semana, festivo

El detalle de cada variable está en [`docs/diccionario_datos.md`](docs/diccionario_datos.md).

Fuente: https://sinca.mma.gob.cl

> **Nota:** en esta fase se utiliza un dataset sintético de demostración que
> reproduce relaciones físicas documentadas de la contaminación en Santiago
> (inversión térmica invernal, ventilación por viento, ciclo diario por
> transporte y calefacción a leña). Para conclusiones definitivas deben usarse
> datos reales descargados del SINCA.

## Estructura del repositorio

\`\`\`
calidad-aire-santiago/
├── README.md              Descripción del proyecto
├── requirements.txt       Dependencias de Python
├── .gitignore             Archivos ignorados por Git
├── data/
│   ├── raw/               CSV originales del SINCA (no se versionan)
│   └── processed/         Datos limpios listos para análisis
├── notebooks/
│   └── 01_exploracion.ipynb   Exploración inicial de los datos
├── src/
│   └── limpieza.py        Funciones de carga y limpieza
└── docs/
    ├── diccionario_datos.md   Descripción de las variables
    └── referencias.md         Referencias en formato APA
\`\`\`

## Cómo reproducir el análisis

\`\`\`bash
git clone https://github.com/usuario/calidad-aire-santiago.git
cd calidad-aire-santiago
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/01_exploracion.ipynb
\`\`\`

El CSV usa punto y coma como separador y coma decimal (formato SINCA):

\`\`\`python
df = pd.read_csv('../data/raw/sinca_santiago.csv',
                 sep=';', decimal=',', encoding='latin-1')
\`\`\`

## Herramientas

- Python 3.11 (pandas, numpy, matplotlib, seaborn)
- Jupyter Notebooks
- Git / GitHub para control de versiones y colaboración

## Referencia

Ministerio del Medio Ambiente. (2024). *Sistema de Información Nacional de
Calidad del Aire (SINCA)*. https://sinca.mma.gob.cl
