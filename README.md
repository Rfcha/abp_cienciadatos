# Proyecto ABP — Ciencia de Datos Reproducible (MCDI500)

**Curso:** Programación para la Ciencia de Datos  
**Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial Avanzada — UNAB  
**Proyecto:** ABP Ciencia de Datos Reproducible  
**Equipo:** Grupo 3  

## Integrantes

- Rodrigo Chinchón Ayala
- Sergio Fernández Almonacid
- Pablo Villalobos González

---

## 1. Descripción general

Este repositorio consolida el trabajo académico del Grupo 3 para el proyecto ABP del curso **MCDI500**.

El objetivo principal es construir un proyecto de ciencia de datos reproducible, versionado y documentado, aplicando buenas prácticas de:

- organización de repositorios;
- control de versiones con Git y GitHub;
- uso de ramas, Pull Requests y commits convencionales;
- creación de entornos reproducibles;
- análisis exploratorio de datos;
- limpieza, transformación y preparación de datasets;
- documentación técnica y académica del proceso.

El repositorio se organiza en tres proyectos principales:

| Proyecto | Carpeta | Propósito |
|---|---|---|
| F1 | `F1/` | Definición inicial, entorno reproducible, documentación técnica y evidencias. |
| F2 | `F2/` | Obtención, limpieza, transformación y preparación inicial de datos. |
| F3 | `F3-calidad-aire-santiago/` | Proyecto aplicado sobre calidad del aire en Santiago de Chile. |

---

## 2. Proyecto F1 — Definición y entorno reproducible

La carpeta `F1/` contiene la primera fase del proyecto, enfocada en establecer la base técnica, documental y metodológica.

**Entregable principal de F1:** el notebook `F1/notebooks/F1_Definicion.ipynb`, que documenta la definición del problema, los objetivos, la validación del entorno reproducible y la vinculación con el mapa conceptual técnico. El informe formal de la fase está en `F1/docs/informe_sumativa1_Final.md`.

### Objetivos de F1

- Definir el contexto inicial del proyecto.
- Documentar el entorno reproducible.
- Estructurar carpetas, notebooks, fuentes y evidencias.
- Registrar dependencias.
- Dejar evidencia del trabajo colaborativo en GitHub.

### Estructura real

```text
F1/
├── data/                       # datos crudos y procesados de la fase
├── docs/                       # informe_sumativa1_Final.md + PDF de la sumativa
├── evidencias/
├── notebooks/
│   └── F1_Definicion.ipynb     # entregable principal de F1
├── src/
│   ├── f1_utils.py             # funciones de captura y validación del entorno
│   └── utils.py
├── README.md
└── requirements.txt
```

---

## 3. Proyecto F2 — Obtención, limpieza y transformación

La carpeta `F2/` contiene la segunda fase del proyecto, enfocada en el tratamiento inicial de los datos.

**Entregable principal de F2:** el notebook `F2/notebooks/F2_Preprocesamiento.ipynb`, que orquesta y documenta el pipeline de preprocesamiento, apoyado en el módulo `F2/src/preprocessing.py`.

### Objetivos de F2

- Obtener o cargar datos desde fuentes definidas.
- Revisar estructura, tipos de datos y calidad inicial.
- Identificar nulos, duplicados e inconsistencias.
- Aplicar limpieza y transformación.
- Generar salidas reproducibles en `data/processed/`.
- Documentar decisiones técnicas.

### Estructura real

```text
F2/
├── data/
│   ├── raw/dataset_base.csv           # dataset crudo con defectos deliberados
│   └── processed/dataset_procesado.csv # salida del pipeline
├── docs/                              # aporte_metodologico_f2_SFA.md + informe
├── evidencias/
├── notebooks/
│   └── F2_Preprocesamiento.ipynb      # entregable principal de F2
├── src/
│   └── preprocessing.py               # load, profile, clean, transform, validate
├── README.md
└── requirements.txt
```

---

## 4. Proyecto F3 — Calidad del Aire en Santiago

La carpeta `F3-calidad-aire-santiago/` corresponde al proyecto aplicado del repositorio.

Este proyecto busca analizar datos asociados a la calidad del aire en Santiago de Chile, considerando una estructura reproducible de ciencia de datos.

### Objetivos de F3

- Explorar datos de calidad del aire.
- Organizar datos crudos y procesados.
- Documentar el diccionario de datos.
- Ejecutar análisis exploratorio mediante Jupyter Notebook.
- Preparar la base para análisis posteriores, visualización y conclusiones.

### Estructura actual

```text
F3-calidad-aire-santiago/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── diccionario_datos.md
├── notebooks/
│   └── 01_exploracion.ipynb
├── src/
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 5. Estructura general del repositorio

```text
ABP_CIENCIADATOS/
├── .github/
│   └── pull_request_template.md
├── F3-calidad-aire-santiago/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── docs/
│   │   └── diccionario_datos.md
│   ├── notebooks/
│   │   └── 01_exploracion.ipynb
│   ├── src/
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
├── common/
│   ├── src/
│   ├── tests/
│   └── .gitkeep
├── docs/
│   ├── checklist_entrega_semana1.md
│   ├── entorno_reproducible.txt
│   ├── flujo_colaborativo.md
│   └── .gitkeep
├── F1/
│   ├── data/
│   ├── docs/
│   ├── evidencias/
│   ├── notebooks/
│   ├── src/
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
├── F2/
│   ├── data/
│   ├── docs/
│   ├── evidencias/
│   ├── notebooks/
│   ├── src/
│   ├── README.md
│   └── requirements.txt
├── logs/
├── .gitignore
├── .mailmap
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

> Nota técnica: las carpetas `.venv/` y `.ruff_cache/` existen únicamente en el entorno local y **no se versionan** en Git. Están correctamente excluidas mediante `.gitignore` (verificable con `git ls-files .venv`, que no devuelve resultados).

---

## 6. Entorno reproducible

### 6.1 Crear entorno virtual

Desde la raíz del repositorio:

```powershell
python -m venv .venv
```

### 6.2 Activar entorno en Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

### 6.3 Actualizar pip

```powershell
python -m pip install --upgrade pip setuptools wheel
```

### 6.4 Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 6.5 Registrar kernel de Jupyter

```powershell
python -m ipykernel install --user --name abp-cienciadatos --display-name "Python (ABP Ciencia Datos)"
```

### 6.6 Iniciar Jupyter Lab

```powershell
jupyter lab
```

---

## 7. Ejecución recomendada

### F1

Abrir los notebooks y documentos ubicados en:

```text
F1/notebooks/F1_Definicion.ipynb
F1/docs/
F1/evidencias/
```

### F2

Abrir los notebooks y scripts ubicados en:

```text
F2/notebooks/F2_Preprocesamiento.ipynb
F2/src/
F2/data/
```

### F3 — Calidad del Aire Santiago

Abrir:

```text
F3-calidad-aire-santiago/notebooks/01_exploracion.ipynb
```

Ejecutar todas las celdas desde el kernel:

```text
Python (ABP Ciencia Datos)
```

---

## 8. Contribución del equipo

La participación de cada integrante se evidencia mediante los commits individuales registrados en el historial de Git. Durante el desarrollo, el equipo se encontraba en proceso de aprendizaje de Git/GitHub, lo que derivó en configuraciones locales inconsistentes del parámetro `user.name`, generando que un mismo colaborador apareciera bajo múltiples identidades en el historial. Para consolidar la trazabilidad individual, se aplicó un archivo `.mailmap` que normaliza las identidades **sin alterar el historial de commits**. GitHub identifica correctamente a los tres colaboradores reales (sección Contributors).

### 8.1 Contribución por fase

**Fase 1 — Definición y entorno reproducible** (37 commits)

| Integrante | Commits | Participación |
|---|---|---|
| Rodrigo Chinchón Ayala | 22 | 59% |
| Pablo Villalobos González | 12 | 32% |
| Sergio Fernández Almonacid | 3 | 8% |

**Fase 2 — Preprocesamiento de datos** (29 commits)

| Integrante | Commits | Participación |
|---|---|---|
| Rodrigo Chinchón Ayala | 19 | 66% |
| Sergio Fernández Almonacid | 8 | 28% |
| Pablo Villalobos González | 2 | 7% |

### 8.2 Aportes principales por integrante

- **Rodrigo Chinchón Ayala:** estructura del repositorio, configuración del entorno reproducible, diseño y orquestación del pipeline de F2, módulos en `src/` y desarrollo de los notebooks.
- **Pablo Villalobos González:** documentación técnica de F1, desarrollo de la definición del problema y apoyo en la exploración inicial de datos.
- **Sergio Fernández Almonacid:** aporte metodológico (`aporte_metodologico_f2_SFA.md`), revisión del planteamiento del problema, validación de supuestos metodológicos y coherencia entre objetivos, datos y resultados desde perspectivas de gestión.

> El conteo de commits se obtuvo con `git shortlog -s -n -e --all -- F1` y `-- F2`, con las identidades consolidadas vía `.mailmap`.

---

## 9. Flujo colaborativo

El repositorio utiliza un flujo colaborativo basado en ramas, Pull Requests y revisión entre integrantes.

### 9.1 Ramas principales

| Rama | Uso |
|---|---|
| `main` | Rama estable y protegida. Solo contiene versiones revisadas e integradas vía Pull Request. |
| `develop` | Integración del trabajo del equipo antes de pasar a `main`. |
| `feature/*` | Desarrollo de tareas específicas por integrante. |
| `fix/*` | Correcciones puntuales. |
| `docs/*` | Cambios documentales. |

### 9.2 Ejemplos de ramas

```text
feature/f1-entorno-reproducible
feature/f2-limpieza-datos
docs/actualizacion-readme
fix/correccion-requirements
```

---

## 10. Pull Requests

Todo cambio relevante debe integrarse mediante Pull Request. La rama `main` está protegida y no admite push directo.

### Criterios mínimos de un Pull Request

- Describe claramente el cambio realizado.
- Indica a qué fase corresponde: F1, F2 o F3.
- Incluye evidencia cuando corresponda.
- No sube archivos temporales innecesarios.
- No incluye conflictos de merge.
- No rompe la ejecución de notebooks.
- Mantiene actualizado el README o documentación relacionada.
- Es revisado por al menos un integrante del equipo.

El template de Pull Request se encuentra en:

```text
.github/pull_request_template.md
```

---

## 11. Convención de commits

Se utiliza una convención simple y profesional basada en commits semánticos.

| Tipo | Uso | Ejemplo |
|---|---|---|
| `feat` | Nueva funcionalidad | `feat: agrega exploracion inicial de calidad del aire` |
| `fix` | Corrección | `fix: corrige carga de datos nulos` |
| `docs` | Documentación | `docs: actualiza README principal` |
| `refactor` | Reorganización interna | `refactor: ordena estructura de carpetas F2` |
| `test` | Pruebas | `test: agrega validaciones de carga de datos` |
| `chore` | Mantención | `chore: actualiza requirements` |

---

## 12. Validaciones recomendadas

Antes de hacer commit o Pull Request:

```powershell
git status
git diff --check
python -m pip check
python -m pytest
ruff check .
```

Para notebooks:

```powershell
jupyter nbconvert --to notebook --execute F3-calidad-aire-santiago/notebooks/01_exploracion.ipynb --output 01_exploracion_validado.ipynb
```

---

## 13. Buenas prácticas del repositorio

- No versionar `.venv/`.
- No versionar `.ruff_cache/`.
- No subir archivos temporales del sistema.
- Mantener datos crudos en `data/raw/`.
- Mantener datos procesados en `data/processed/`.
- Documentar cambios relevantes.
- Mantener notebooks ejecutables de inicio a fin.
- Evitar conflictos de merge en archivos Markdown.
- Usar nombres de archivos claros y consistentes.
- Mantener `requirements.txt` actualizado.

---

## 14. Estado del proyecto

| Componente | Estado |
|---|---|
| Repositorio GitHub | Implementado |
| README principal | Actualizado |
| `requirements.txt` principal | Actualizado |
| F1 | Implementado |
| F2 | Implementado |
| F3 `F3-calidad-aire-santiago` | En evolución |
| Pull Request template | Implementado |
| Flujo colaborativo | Documentado |
| Entorno reproducible | Documentado |
| Consolidación de autoría (`.mailmap`) | Implementado |
| Diccionario de datos | Implementado |
| Notebook exploratorio F3 | Implementado |

---

## 15. Licencia y uso académico

Este repositorio tiene fines académicos y corresponde al desarrollo del proyecto ABP del Grupo 3 para el curso **MCDI500 — Programación para la Ciencia de Datos**. La licencia se encuentra en el archivo `LICENSE`.
