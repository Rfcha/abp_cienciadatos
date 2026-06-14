# Calidad del Aire en Santiago: Detección de Episodios Críticos de MP2.5 mediante Ciencia de Datos y Algoritmos Eficientes

## MCDI500 – Herramientas de Software Científico

### Magíster en Ciencia de Datos e Inteligencia Artificial – Universidad Andrés Bello

**Proyecto Transversal – Grupo 3**

**Integrantes**

* Rodrigo Chinchón Ayala
* Sergio Fernández Almonacid
* Pablo Villalobos González

---

# 1. Resumen Ejecutivo

La contaminación atmosférica por material particulado fino (MP2.5) representa uno de los principales problemas ambientales y de salud pública en la Región Metropolitana de Santiago.

Este proyecto desarrolla un flujo reproducible de Ciencia de Datos para identificar, caracterizar y analizar episodios críticos de contaminación atmosférica utilizando datos horarios provenientes de la red oficial SINCA (Sistema de Información Nacional de Calidad del Aire).

El trabajo se estructura progresivamente en tres fases:

* **Fase 1:** definición conceptual, entorno reproducible y control de versiones.
* **Fase 2:** exploración, limpieza, transformación y análisis exploratorio de datos.
* **Fase 3:** construcción del núcleo algorítmico mediante programación estructurada, algoritmos recursivos, análisis de complejidad computacional y aplicación de Programación Orientada a Objetos (POO).

El objetivo final es construir una base técnica sólida para futuras fases de modelamiento predictivo y aprendizaje automático.

---

# 2. Pregunta de Investigación

> ¿Qué condiciones meteorológicas están asociadas a la ocurrencia de episodios críticos de contaminación por material particulado fino (MP2.5) en Santiago de Chile?

---

# 3. Objetivos

## Objetivo General

Analizar la relación entre variables meteorológicas y los episodios críticos de contaminación atmosférica por MP2.5 en Santiago mediante técnicas reproducibles de Ciencia de Datos y algoritmos eficientes.

## Objetivos Específicos

* Procesar datos horarios provenientes del SINCA.
* Construir un pipeline reproducible de limpieza y transformación.
* Detectar episodios críticos de contaminación.
* Implementar algoritmos recursivos para búsqueda y ordenamiento.
* Comparar eficiencia computacional mediante análisis temporal.
* Aplicar principios de encapsulamiento, herencia y polimorfismo.
* Documentar técnicamente el sistema y su arquitectura.

---

# 4. Dataset Utilizado

## Fuente Oficial

Sistema de Información Nacional de Calidad del Aire (SINCA)

https://sinca.mma.gob.cl

## Cobertura

* Región Metropolitana de Santiago
* Periodo analizado: 2022–2023
* Frecuencia: Horaria

## Volumen

* 192.720 registros
* 11 estaciones de monitoreo
* Más de 15 variables ambientales

## Comunas Analizadas

* Cerrillos
* Cerro Navia
* El Bosque
* Independencia
* La Florida
* Las Condes
* Providencia
* Puente Alto
* Pudahuel
* Quilicura
* Talagante

## Variables Principales

### Contaminantes

* MP2.5
* MP10

### Meteorológicas

* Temperatura
* Humedad relativa
* Presión atmosférica
* Velocidad del viento
* Radiación solar
* Inversión térmica

### Temporales

* Fecha
* Hora
* Día de semana
* Fin de semana
* Festivos

---

# 5. Desarrollo por Fases

## Fase 1 – Preparación del Proyecto

Objetivo:

Construir una base reproducible para el desarrollo colaborativo.

Actividades:

* Configuración de entorno Python.
* Git y GitHub.
* Estructura de carpetas.
* Definición de estándares.
* Documentación inicial.
* Gestión colaborativa mediante ramas y Pull Requests.

---

## Fase 2 – Exploración y Preparación de Datos

Objetivo:

Comprender y preparar el dataset para análisis posteriores.

Actividades:

* Carga de datos.
* Limpieza de registros.
* Tratamiento de valores faltantes.
* Imputación mediante mediana.
* Análisis exploratorio.
* Visualizaciones estadísticas.
* Correlaciones.
* Análisis temporal.
* Construcción de variables derivadas.

Notebook:

`01_exploracion.ipynb`

---

## Fase 3 – Núcleo Algorítmico

Objetivo:

Implementar soluciones algorítmicas eficientes utilizando programación estructurada, recursividad y POO.

Actividades:

### Programación Funcional

* Detección de episodios críticos.
* Procesamiento modular.
* Separación de responsabilidades.

### Algoritmos Recursivos

#### Búsqueda Binaria

Complejidad:

O(log n)

Objetivo:

Localizar el primer valor que supera un umbral crítico.

#### Merge Sort

Complejidad:

O(n log n)

Objetivo:

Ordenamiento eficiente de concentraciones de MP2.5.

### Análisis de Complejidad

Comparaciones realizadas:

* Búsqueda lineal vs búsqueda binaria.
* Bucle Python vs vectorización NumPy.

Herramienta utilizada:

* timeit

### Programación Orientada a Objetos

Implementación de:

* Encapsulamiento
* Herencia
* Polimorfismo
* Clases abstractas
* Método plantilla (Template Method)

---

# 6. Arquitectura de Software

## Jerarquía de Clases

```text
AnalizadorBase (ABC)
│
├── AnalizadorMP25
│     ├── merge_sort_recursivo()
│     └── busqueda_binaria_recursiva()
│
└── AnalizadorMP10
```

## Responsabilidades

### AnalizadorBase

* Contrato común del sistema.
* Encapsulamiento de datos.
* Estadísticas generales.
* Método plantilla.

### AnalizadorMP25

* Análisis especializado de MP2.5.
* Algoritmos recursivos.
* Detección de episodios críticos.

### AnalizadorMP10

* Análisis especializado de MP10.
* Reutilización del comportamiento base.

---

# 7. Estructura del Repositorio

```text
F3-calidad-aire-santiago
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_exploracion.ipynb
│   └── 02_algoritmos.ipynb
│
├── src
│   ├── limpieza.py
│   └── algoritmos.py
│
└── docs
    ├── referencias.md
    └── diccionario_datos.md
```

---

# 8. Reproducibilidad

## Clonar Repositorio

```bash
git clone https://github.com/Rfcha/abp_cienciadatos.git
```

```bash
cd abp_cienciadatos/F3-calidad-aire-santiago
```

## Crear Entorno Virtual

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
jupyter lab
```

Ejecutar los notebooks en orden:

1. `01_exploracion.ipynb`
2. `02_algoritmos.ipynb`

utilizando:

```text
Kernel → Restart & Run All
```

---

# 9. Flujo de Trabajo Colaborativo

## Estrategia Git

```text
main
 │
 └── dev
      │
      ├── feature/rodrigo
      ├── feature/pablo
      └── feature/sergio
```

## Convención de Commits

```text
feat:
fix:
docs:
refactor:
test:
chore:
```

## Integración

* Pull Request obligatorio.
* Revisión cruzada.
* Merge hacia dev.
* Liberación controlada hacia main.

---

# 10. Resultados Técnicos Relevantes

Durante la Fase 3 se verificó que:

* La búsqueda binaria supera ampliamente a la búsqueda lineal para localizar umbrales críticos.
* La vectorización mediante NumPy reduce significativamente los tiempos de ejecución respecto a bucles Python tradicionales.
* La arquitectura orientada a objetos mejora la mantenibilidad y escalabilidad del sistema.
* La recursividad permite implementar algoritmos clásicos con complejidad óptima.

---

# 11. Trabajo Futuro

Fase 4:

* Modelamiento predictivo.
* Machine Learning supervisado.
* Predicción de episodios críticos.
* Evaluación de modelos.
* Métricas de desempeño.
* Interpretabilidad de resultados.

---

# 12. Referencias

1.- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2.- Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. *Nature*, 585, 357–362.
3.- McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
4.- Ministerio del Medio Ambiente. (2024). Sistema de Información Nacional de Calidad del Aire (SINCA). https://sinca.mma.gob.cl
5.- Python Software Foundation. (2024). Python Standard Library – timeit. https://docs.python.org/3/library/timeit.html
6.- The pandas development team. (2024). pandas documentation. https://pandas.pydata.org/docs/
