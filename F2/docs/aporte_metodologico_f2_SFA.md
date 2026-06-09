# Aporte metodológico F2 - SFA

## 1. Propósito del aporte

Este documento registra una contribución metodológica para la Fase 2 del proyecto, orientada a fortalecer la comprensión del proceso de obtención, limpieza y transformación de datos.

La finalidad es apoyar la trazabilidad del pipeline de preprocesamiento, facilitando que los cambios realizados sobre el dataset puedan ser comprendidos, revisados y justificados por integrantes técnicos y no técnicos.

## 2. Enfoque de la Fase 2

La Fase 2 se centra en preparar los datos para su posterior análisis, asegurando que el dataset procesado sea más consistente, confiable y útil para las siguientes etapas del proyecto.

En esta etapa se revisan aspectos como:

- Datos nulos.
- Registros duplicados.
- Tipos de datos.
- Normalización de texto.
- Validación del dataset procesado.

## 3. Preguntas orientadoras para revisar la limpieza de datos

Para fortalecer la calidad del proceso, se proponen las siguientes preguntas:

- ¿Qué columnas presentan valores nulos?
- ¿Los valores nulos fueron tratados con un criterio claro?
- ¿Existen registros duplicados?
- ¿Los duplicados eliminados corresponden realmente a registros repetidos?
- ¿Los tipos de datos son coherentes con el significado de cada variable?
- ¿El dataset final conserva información suficiente para el análisis?

## 4. Preguntas orientadoras para revisar la transformación de datos

Además de limpiar los datos, es importante revisar si las transformaciones aplicadas son comprensibles.

Preguntas sugeridas:

- ¿Qué variables numéricas fueron normalizadas?
- ¿Qué variables categóricas fueron codificadas?
- ¿Existe una diferencia clara entre el dataset crudo y el dataset procesado?

## 5. Aporte a la trazabilidad

Una buena práctica en proyectos de ciencia de datos es documentar no solo el resultado final, sino también las decisiones tomadas durante el preprocesamiento.

Por ello, se recomienda dejar registro de:

- Qué datos fueron modificados.
- Qué criterios se usaron para limpiar o transformar variables.
- Qué supuestos se aplicaron.
- Qué limitaciones permanecen después de la limpieza.
- Qué riesgos interpretativos podrían existir.
- Qué validaciones confirman que el dataset procesado es utilizable.

## 6. Valor para el proyecto

El aporte busca fortalecer la calidad documental de la Fase 2, apoyando la comunicación entre los integrantes del equipo, sean expertos o no.

Desde una mirada no experta en programación, esta contribución ayuda a conectar el proceso técnico de limpieza y transformación con criterios de comprensión, trazabilidad y utilidad para el análisis posterior.