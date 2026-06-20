# Changelog — Proyecto ABP Ciencia de Datos

**Repositorio:** `Rfcha/abp_cienciadatos`
**Proyecto:** Calidad del Aire en Santiago — Detección de Episodios Críticos de MP2.5
**Asignatura:** MCDI500 — Programación para la Ciencia de Datos
**Equipo (Grupo 3):** Rodrigo Chinchón Ayala · Sergio Fernández Almonacid · Pablo Villalobos González
**Docente:** Dr. Omar Salinas Silva

Este documento registra la evolución técnica del proyecto a lo largo de las cuatro fases del
Aprendizaje Basado en Proyectos (F1 → F4), documentando para cada cambio relevante: la fecha,
una descripción de la mejora, el commit asociado y su justificación técnica. Complementa la
sección «Trazabilidad de mejoras» del informe final y de los notebooks.

El formato sigue, de forma adaptada, la convención
[Keep a Changelog](https://keepachangelog.com/es/1.1.0/).

> **Nota:** los identificadores de commit mostrados como `abc123` son marcadores de referencia.
> Antes de la entrega final deben reemplazarse por los hash reales verificados con
> `git log --oneline`, manteniendo la coherencia con la tabla de trazabilidad del informe.

---

## [F4 — Entrega final] — Análisis, reproducibilidad y comunicación · 2026-06-21

### Añadido
- Secciones de cierre **Resultados**, **Discusión**, **Conclusiones** y **Trazabilidad de mejoras**
  en ambos notebooks (`01_exploracion.ipynb` y `02_algoritmos.ipynb`). · `abc123`
  *Justificación técnica:* la Fase 4 integra y comunica los hallazgos; estas secciones cierran el
  relato analítico (storytelling) exigido por la rúbrica y vinculan resultados con objetivos.
- Archivo `changelog.md` con la trazabilidad técnica completa F1 → F4. · `def456`
  *Justificación técnica:* evidencia verificable de la evolución del proyecto y de la incorporación
  de observaciones formativas.
- Informe técnico final en formato institucional (PDF) integrando las cuatro fases. · `ghi789`
  *Justificación técnica:* consolida en un solo documento entorno, datos, núcleo algorítmico y
  comunicación de resultados, en correspondencia con el repositorio.

### Cambiado
- Títulos y referencias de los notebooks actualizados de «Fase 3» a
  **«Fase 4 Entrega final»**, preservando el nombre del repositorio y las rutas. · `jkl012`
  *Justificación técnica:* coherencia entre el entregable final y la nomenclatura de la fase,
  sin romper la reproducibilidad de rutas y dependencias.

### Corregido
- Normalización de la numeración de secciones y de identificadores de celda en los notebooks. · `mno345`
  *Justificación técnica:* asegura ejecución limpia de inicio a fin (Restart & Run All) y validez
  `nbformat`, requisito de reproducibilidad.

---

## [F3 — Desarrollo] — Núcleo algorítmico · 2026-06-14

### Añadido
- Implementación de **búsqueda binaria recursiva** para localizar el umbral crítico de MP2.5. · `pqr678`
  *Justificación técnica:* complejidad O(log n) frente a O(n) de la búsqueda lineal; reduce
  comparaciones de forma medible.
- Implementación de **merge sort recursivo** para ordenar horas por concentración de MP2.5. · `stu901`
  *Justificación técnica:* ordenamiento estable O(n log n) que habilita el ranking de periodos críticos.
- **Programación Orientada a Objetos**: clase abstracta base, herencia y polimorfismo para el
  modelado del episodio crítico. · `vwx234`
  *Justificación técnica:* mejora la modularidad, mantenibilidad y extensibilidad del núcleo.
- **Benchmarks reproducibles** con `timeit` (búsqueda lineal vs. binaria; bucle Python vs. NumPy). · `yza567`
  *Justificación técnica:* mediciones formales y verificables para justificar las decisiones de optimización.

### Corregido
- Incorporación de **manejo de excepciones y validación de casos límite** en el núcleo algorítmico. · `bcd890`
  *Justificación técnica:* responde a la observación formativa de reforzar las validaciones;
  aumenta la robustez y trazabilidad de las pruebas.
- Rediseño de las celdas de presentación a un **esquema institucional GitHub-safe**
  (colores sólidos, sin gradientes oscuros ni texto blanco, tamaños fijos). · `efg123`
  *Justificación técnica:* el sanitizador HTML de GitHub eliminaba estilos y producía texto
  invisible; el rediseño garantiza legibilidad en Jupyter, PDF y GitHub.

---

## [F2 — Obtención y transformación] — Preprocesamiento de datos · 2026-06-07

### Añadido
- Módulo `preprocessing.py` con el pipeline completo: carga, perfilado, limpieza,
  transformación y validación. · `hij456`
  *Justificación técnica:* separa la lógica reutilizable del notebook (alta cohesión, bajo acoplamiento)
  y asegura un flujo de datos verificable.
- Salida reproducible `data/processed/dataset_procesado.csv`. · `klm789`
  *Justificación técnica:* dataset íntegro y trazable, apto para los análisis posteriores.

### Corregido
- **Auto-detección de separador y codificación** en la carga de CSV de la red SINCA
  (`;` / `,`, `latin-1` / `utf-8`). · `nop012`
  *Justificación técnica:* resuelve un `KeyError: 'MP2.5'` originado por el formato no estándar de
  los archivos SINCA; hace la carga defensiva y reproducible.
- Manejo riguroso de valores NA, casting de tipos y normalización de variables. · `qrs345`
  *Justificación técnica:* responde a la observación formativa de justificar técnicamente cada
  transformación; mejora la consistencia del dataset.

---

## [F1 — Definición y entorno] — Entorno reproducible · 2026-05-31

### Añadido
- Estructura inicial del repositorio (`F1/`, `F2/`, `F3-calidad-aire-santiago/`, `common/`, `docs/`). · `tuv678`
  *Justificación técnica:* organización coherente por fases, alineada con prácticas profesionales y con el informe.
- **Entorno reproducible**: `requirements.txt`, scripts de creación de entorno virtual y registro de
  kernel de Jupyter. · `wxy901`
  *Justificación técnica:* garantiza que el proyecto se ejecute sin errores en cualquier equipo.
- Estándares de comunidad: `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`,
  `.gitignore` y `.mailmap`. · `zab234`
  *Justificación técnica:* habilita colaboración trazable entre los tres integrantes y consolida la
  identidad de autoría en el historial de Git.
- Notebook `F1_Definicion.ipynb` con la definición del problema, objetivos y mapa conceptual. · `cde567`
  *Justificación técnica:* documenta el punto de partida y la vinculación entre fases.

---

## Síntesis del impacto de las mejoras

| Dimensión | Evolución a lo largo de F1 → F4 |
|---|---|
| **Modularidad** | De scripts iniciales a módulos reutilizables (`preprocessing.py`) y diseño POO con herencia y polimorfismo. |
| **Rendimiento** | Incorporación de algoritmos O(log n) y O(n log n) y vectorización NumPy, con mediciones `timeit` reproducibles. |
| **Reproducibilidad** | Entorno virtual, dependencias controladas, carga de datos defensiva y ejecución limpia de inicio a fin. |
| **Documentación** | De documentación básica a notebooks con storytelling, informe institucional y este changelog trazable. |

---

*Última actualización: 2026-06-21 · Generado para la Evaluación Sumativa 4 (Fase 4) — MCDI500.*
