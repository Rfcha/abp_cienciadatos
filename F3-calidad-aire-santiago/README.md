# Calidad del aire en Santiago

Proyecto aplicado — MCDI500. Análisis de la relación entre variables
meteorológicas y los episodios críticos de contaminación por material particulado
(MP2.5 / MP10) en la Región Metropolitana, con un flujo reproducible de ciencia de
datos que abarca exploración, preprocesamiento y un núcleo algorítmico.

## Integrantes (Grupo 3)

- Rodrigo Chinchón Ayala
- Sergio Fernández Almonacid
- Pablo Villalobos González

## Problema

¿Qué condiciones meteorológicas anticipan un episodio crítico de contaminación
por material particulado en Santiago? El proyecto identifica las condiciones
(temperatura, viento, presión, inversión térmica) asociadas a las horas en que
el MP2.5 supera el umbral crítico, y desarrolla algoritmos para detectar y
caracterizar esos episodios de forma eficiente.

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

> **Nota sobre los datos:** en esta fase se utiliza un dataset sintético de
> demostración que reproduce relaciones físicas documentadas de la contaminación
> en Santiago (inversión térmica invernal, ventilación por viento, ciclo diario
> por transporte y calefacción a leña). Para conclusiones definitivas deben
> usarse datos reales descargados del SINCA.

> **Nota sobre el versionamiento:** como buena práctica en ciencia de datos, los
> datos crudos normalmente **no** se versionan en Git (suelen ser pesados y
> cambiar con frecuencia). En este repositorio se incluye el CSV de demostración
> en `data/raw/` para facilitar la revisión de la entrega; la regla
> correspondiente queda comentada en `.gitignore`.

## Fases del proyecto

Este proyecto aplicado se desarrolla en notebooks sucesivos dentro de
`notebooks/`, cada uno construyendo sobre el anterior:

| Notebook | Contenido | Apartados de rúbrica |
|---|---|---|
| `01_exploracion.ipynb` | Carga, limpieza, definición del episodio crítico, panel exploratorio, correlaciones y conclusiones preliminares. | Exploración y preprocesamiento. |
| `02_algoritmos.ipynb` | Núcleo algorítmico: funciones modulares, algoritmos recursivos (búsqueda binaria y merge sort), mediciones de complejidad con `timeit`, clase `AnalizadorAire` y documentación de arquitectura. | Codificación funcional, eficiencia, modularidad, recursividad. |

> **Procedencia del dataset para el análisis algorítmico:** el notebook
> `02_algoritmos.ipynb` parte del dataset procesado **de este mismo proyecto**
> (`data/processed/sinca_limpio.csv`), no del dataset de práctica de la carpeta
> `F2/` del repositorio. La carpeta `F2/` corresponde a una sumativa previa del
> curso con un dataset genérico, sin relación con los datos del SINCA.

## Estructura del repositorio

```text
F3-calidad-aire-santiago/
├── README.md                  Descripción del proyecto
├── requirements.txt           Dependencias de Python
├── .gitignore                 Archivos ignorados por Git
├── data/
│   ├── raw/                   CSV originales del SINCA
│   │   └── sinca_santiago.csv
│   └── processed/             Datos limpios listos para análisis
│       └── sinca_limpio.csv
├── notebooks/
│   ├── 01_exploracion.ipynb   Exploración inicial de los datos
│   └── 02_algoritmos.ipynb    Núcleo algorítmico (Fase 3)
├── src/
│   ├── limpieza.py            Funciones de carga y limpieza
│   └── algoritmos.py          Funciones algorítmicas reutilizables (opcional)
└── docs/
    ├── diccionario_datos.md   Descripción de las variables
    └── referencias.md         Referencias en formato APA
```

## Cómo reproducir el análisis

```bash
git clone https://github.com/usuario/abp_cienciadatos.git
cd abp_cienciadatos/F3-calidad-aire-santiago
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Ejecutar los notebooks en orden (`01_exploracion.ipynb` → `02_algoritmos.ipynb`)
con `Restart & Run All`.

El CSV usa punto y coma como separador y coma decimal (formato SINCA):

```python
df = pd.read_csv('data/raw/sinca_santiago.csv',
                 sep=';', decimal=',', encoding='latin-1')
```

## Núcleo algorítmico (Fase 3)

El notebook `02_algoritmos.ipynb` implementa, sobre la columna MP2.5 y el umbral
de 50 µg/m³:

- **Búsqueda binaria recursiva** del primer cruce del umbral — O(log n).
- **Merge sort recursivo** de las concentraciones — O(n log n).
- **Detección de episodios como rachas** de horas consecutivas sobre el umbral.
- **Dos comparaciones de complejidad** con `timeit`: búsqueda lineal vs binaria, y
  bucle Python vs operación vectorizada.
- **Clase `AnalizadorAire`** que encapsula datos, umbral y métodos de análisis.

## Herramientas

- Python 3.11 (pandas, numpy, matplotlib)
- Jupyter Lab / Notebooks
- `timeit` (biblioteca estándar) para mediciones de complejidad
- Git / GitHub para control de versiones y colaboración

## Referencias

- Ministerio del Medio Ambiente. (2024). *Sistema de Información Nacional de
  Calidad del Aire (SINCA)*. https://sinca.mma.gob.cl
- McKinney, W. (2022). *Python for Data Analysis* (3.ª ed.). O'Reilly Media.
- The pandas development team. (2024). *pandas documentation*. https://pandas.pydata.org/docs/
- Python Software Foundation. (2024). *The Python standard library — timeit*. https://docs.python.org/3/library/timeit.html
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4.ª ed.). MIT Press.
