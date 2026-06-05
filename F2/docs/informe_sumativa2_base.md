# Informe Sumativa 2 - Fase 2

## Portada
- Curso: Programacion para la Ciencia (202681.2535)
- Proyecto: Proyecto ABP - Ciencia de Datos Reproducible
- Integrantes:
- Rodrigo Chinchon
- Pablo Villalobos
- Sergio Fernandez
- Docente: Dr. Omar Salinas Silva
- Fecha: 2026-06-01

## Introduccion
La Fase 2 implementa el pipeline inicial de obtencion, limpieza, transformacion y validacion de datos, manteniendo coherencia con la definicion tecnica de F1.

## Diseno de soluciones algoritmicas eficientes
- Funciones con parametros claros en F2/src/preprocessing.py.
- Separacion de responsabilidades: carga, perfilamiento, limpieza, transformacion, validacion y persistencia.
- Flujo verificable desde dataset raw hasta dataset processed.

## Preprocesamiento y transformacion
- Manejo de NA numericos con mediana.
- Manejo de NA categoricos con No informado.
- Eliminacion de duplicados.
- Casting de tipos.
- Normalizacion MinMax de variables numericas.
- One Hot Encoding de categoricas nominales.

## Validacion tecnica
- Ausencia de nulos.
- Ausencia de duplicados.
- Generacion de archivo procesado.
- Trazabilidad en notebook y repositorio.

## Notebook ejecutable
F2/notebooks/F2_Preprocesamiento.ipynb

## Repositorio GitHub
Actualizar README, commits por integrante e historial trazable.

## Bibliografia APA 7
1. Documentacion oficial de Python.
2. Documentacion oficial de Pandas.
3. Documentacion oficial de NumPy.
4. Documentacion oficial de scikit-learn.
5. Material docente del curso UNAB.