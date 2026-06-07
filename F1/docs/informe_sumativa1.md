# Informe Sumativa 1 - Fase 1
## Portada
- Curso: Programacion para la Ciencia (202681.2535)
- Proyecto: Proyecto ABP - Ciencia de Datos Reproducible
- Integrantes: Pablo Villalobos / Rodrigo Chinchon / Sergio Fernandez
- Docente: Dr. Omar Salinas Silva
- Fecha: 2026-06-01

## Introduccion y contextualizacion
El desarrollo de proyectos de Ciencia de Datos requiere entornos de trabajo reproducibles que permitan garantizar la consistencia de los resultados, la colaboración entre integrantes y la trazabilidad de las decisiones técnicas adoptadas durante el ciclo de vida del proyecto. En contextos académicos y profesionales, la ausencia de mecanismos de control de versiones, documentación técnica y gestión estructurada de dependencias puede generar dificultades para reproducir experimentos, validar resultados y mantener la continuidad del trabajo colaborativo.

En este contexto, el presente proyecto corresponde a la implementación inicial del entorno reproducible del Proyecto ABP de Ciencia de Datos Reproducible del curso Programación para la Ciencia. Durante esta primera fase se establecen los componentes técnicos fundamentales que permitirán desarrollar las etapas posteriores del proyecto, incluyendo la estructura del repositorio GitHub, la configuración del ambiente virtual, la gestión de dependencias, la documentación técnica y la construcción del notebook inicial de trabajo.

La relevancia de esta fase radica en que constituye la base metodológica y tecnológica sobre la cual se desarrollarán los procesos de exploración, limpieza, transformación y análisis de datos en las fases siguientes. De esta forma, F1 establece el entorno reproducible; F2 abordará la exploración inicial de datos; F3 desarrollará los procesos de preparación y análisis; y F4 consolidará los resultados y conclusiones del proyecto.

## Problemática
Uno de los principales desafíos en los proyectos de Ciencia de Datos es asegurar la reproducibilidad técnica de los procesos analíticos y computacionales. La falta de estandarización en entornos de desarrollo, versiones de librerías, documentación y control de cambios dificulta la colaboración efectiva entre integrantes y la capacidad de replicar resultados obtenidos en diferentes equipos o momentos del proyecto.

## Preguntas centrales
- ¿Cómo implementar un entorno reproducible que garantice la ejecución consistente del proyecto?
- ¿Qué herramientas permiten asegurar trazabilidad y colaboración durante el desarrollo?
- ¿Cómo documentar adecuadamente el entorno y los componentes técnicos para facilitar la continuidad de las fases posteriores?

## Objetivo general
Implementar un entorno reproducible para el desarrollo de proyectos de Ciencia de Datos utilizando Python, Jupyter Notebook, Git y GitHub, garantizando trazabilidad, documentación técnica y colaboración efectiva entre los integrantes del equipo.

## Objetivos específicos
1. Configurar un ambiente virtual de desarrollo reproducible.
2. Gestionar las dependencias del proyecto mediante un archivo requirements.txt.
3. Implementar un notebook inicial que documente la problemática y los objetivos del proyecto.
4. Establecer un repositorio GitHub con estructura organizada y control de versiones.
5. Documentar técnicamente la configuración inicial para asegurar continuidad en las fases posteriores.

## Alcance
La Fase 1 contempla exclusivamente la implementación del entorno reproducible y la documentación técnica inicial. No incluye aún procesos avanzados de limpieza, transformación, modelamiento o visualización de datos.

## Supuestos
* Las librerías declaradas en requirements.txt son suficientes para las actividades iniciales.
* Todos los integrantes utilizan versiones compatibles del entorno Python.
* El repositorio GitHub será utilizado como fuente oficial de control de versiones durante el proyecto.

## Aplicación de herramientas científicas
La implementación de la Fase 1 utiliza herramientas fundamentales del ecosistema científico de Python. NumPy proporciona capacidades para operaciones numéricas eficientes; Pandas permite la manipulación y estructuración de datos; Matplotlib habilita futuras capacidades de visualización; y Scikit-learn constituye la base para procesos posteriores de análisis y modelamiento.

La documentación computacional se realiza mediante Jupyter Notebook, permitiendo integrar texto, código y resultados en un único entorno reproducible. Asimismo, Git y GitHub son utilizados para gestionar el control de versiones, registrar cambios y facilitar el trabajo colaborativo entre los integrantes del proyecto.

## Aplicacion de herramientas cientificas
Python, Jupyter, NumPy, Pandas, Matplotlib, Git/GitHub.

## Reproducibilidad tecnica
El proyecto utiliza un ambiente virtual independiente para garantizar la consistencia de ejecución entre diferentes equipos.
| Componente | Versión |
| ---------- | ------- |
| Python     | 3.12.10 |
| NumPy      | 2.4.6   |
| Pandas     | 3.0.3   |
| Matplotlib | 3.10.9  |
| JupyterLab | 4.5.7   |

## Activación del entorno
Windows            PowerShell   .\.venv\Scripts\Activate.ps1
Linux / MAC        Bash         source .venv/bin/activate

Las dependencias utilizadas en esta fase se encuentran registradas en requirements.txt, permitiendo reproducir el entorno mediante la instalación automatizada de paquetes.

## Control de versiones
El proyecto utiliza Git y GitHub como mecanismo oficial de control de versiones. Todas las modificaciones realizadas durante la Fase 1 son registradas mediante commits descriptivos que permiten identificar cambios, responsables y evolución del proyecto.

La estructura colaborativa considera el uso de ramas, integración mediante Pull Requests y documentación de cambios significativos, asegurando trazabilidad y gobernanza técnica durante todo el ciclo de vida del proyecto.

Importante: aquí se deben registrar evidencia de los commits y pull request realizados por:
1. Rodrigo Chinchón Ayala
2. Pablo Villalobos González
3. Sergio Fernández Almonacid

## Notebook F1_Definicion.ipynb
El notebook F1_Definicion.ipynb constituye la evidencia principal de la implementación inicial del proyecto. Su propósito es documentar la problemática, los objetivos, la validación del entorno y la estructura metodológica que guiará el desarrollo de las fases posteriores.

El notebook incorpora narrativa técnica, validación de dependencias y evidencia de ejecución reproducible dentro del entorno configurado, manteniendo coherencia con el informe técnico y el repositorio GitHub.

## Documentación del proceso
Durante la Fase 1 se definieron las decisiones técnicas fundamentales para garantizar reproducibilidad y colaboración.

Entre las principales decisiones adoptadas se encuentran:
- Uso de Python como lenguaje principal.
- Implementación de entorno virtual independiente.
- Gestión centralizada de dependencias mediante requirements.txt.
- Utilización de Jupyter Notebook para documentación computacional.
- Control de versiones mediante Git y GitHub.
- Organización modular del repositorio siguiendo buenas prácticas de Ciencia de Datos.

Estas decisiones permitirán mantener consistencia metodológica y facilitar la continuidad del trabajo durante las fases posteriores.

## Repositorio GitHub correspondiente a la Fase 1
El repositorio fue estructurado siguiendo criterios de reproducibilidad y organización documental.

Incluye:
Notebook F1_Definicion.ipynb.
Archivo README.md.
Archivo requirements.txt.
Documentación técnica asociada.
Estructura preparada para futuras fases del proyecto.

La organización adoptada permite mantener separación clara entre código fuente, documentación, notebooks y recursos asociados, facilitando la trazabilidad y el mantenimiento del proyecto

## Vinculacion con mapa conceptual
Tabla: componente del mapa, evidencia implementada, archivo asociado y fase futura.
| Componente del mapa conceptual | Fase | Evidencia                           |
| ------------------------------ | ---- | ----------------------------------- |
| Entorno reproducible           | F1   | Ambiente virtual + requirements.txt |
| Control de versiones           | F1   | Git y GitHub                        |
| Notebook científico            | F1   | F1_Definicion.ipynb                 |
| Documentación técnica          | F1   | README.md e informe                 |
| Exploración de datos           | F2   | En Desarrollo                       |
| Limpieza y transformación      | F3   | En Desarrollo                       |
| Visualización y análisis       | F3   | En Desarrollo                       |
| Conclusiones y reporte final   | F4   | Desarrollo futuro                   |


## Bibliografia APA 7
1. Python Software Foundation. (2024). Python 3.12 Documentation. https://docs.python.org/3.12/
2. Project Jupyter. (2024). Jupyter Documentation. https://docs.jupyter.org/
3. The Pandas Development Team. (2024). Pandas Documentation. https://pandas.pydata.org/docs/
4. Harris, C. R., et al. (2020). Array programming with NumPy. Nature, 585(7825), 357-362.
5. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
6. Universidad Andrés Bello. (2026). Programación para la Ciencia – Material de apoyo y guía metodológica del curso.