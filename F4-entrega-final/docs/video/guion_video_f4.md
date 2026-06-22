# GUIÓN — VIDEO FASE 4 (ENTREGA FINAL)
## Proyecto: Calidad del Aire en Santiago — Detección de Episodios Críticos de MP2.5
### MCDI500 · Grupo 3 · Duración objetivo: 5–8 min (apuntar a ≈6:30)

> **Cómo usar este guión:** lee a ritmo conversacional, no corrido. Las líneas en
> **MAYÚSCULAS entre corchetes** son indicaciones de cámara/pantalla, NO se leen.
> Cada bloque indica quién habla y su tiempo. Pausa breve donde hay punto y aparte.

---

# ════════════════════════════════════════════
# BLOQUE 1 — RODRIGO (≈ 2:30)
# Secciones: 1. Introducción · 2. Datos · 3. Metodología
# ════════════════════════════════════════════

**[CÁMARA: Rodrigo · PANTALLA: portada del proyecto]**

Hola. Somos el Grupo 3 del Magíster en Ciencia de Datos e Inteligencia Artificial.

Soy Rodrigo Chinchón, y me acompañan Sergio Fernández y Pablo Villalobos.

Hoy presentamos nuestro proyecto final: la detección de episodios críticos
de material particulado fino, el MP2.5, en Santiago.

**[PANTALLA: contexto Santiago — smog]**

El problema es real y cercano. Cada año Santiago vive episodios de
contaminación atmosférica que afectan la salud de las personas,
sobre todo en los meses fríos.

Nuestra pregunta fue clara:
¿podemos detectar de forma automática y eficiente cuándo ocurre un episodio
crítico de MP2.5, y entender con qué condiciones se relaciona?

**[PANTALLA: sección 2 — Datos / fuente SINCA]**

Para responderla, trabajamos con datos reales de la red SINCA,
el Sistema de Información Nacional de Calidad del Aire.

Las variables principales son las concentraciones de material particulado
—MP2.5 y MP10— junto a variables meteorológicas asociadas.

Antes de analizar, ejecutamos una etapa rigurosa de preparación:
limpieza, manejo de valores faltantes, normalización y validación.
El resultado es una base íntegra y completamente reproducible.

**[PANTALLA: sección 3 — Metodología / notebooks]**

Metodológicamente, estructuramos el trabajo en cuatro etapas.

Primero, la exploración de datos, para caracterizar el comportamiento del MP2.5.

Segundo, la implementación de algoritmos eficientes:
una búsqueda binaria recursiva para localizar el umbral crítico,
y un merge sort recursivo para ordenar las horas por concentración.

Tercero, las validaciones técnicas:
casos normales, casos límite y excepciones.

Y cuarto, la reproducibilidad:
entorno virtual documentado, dependencias controladas
y todo versionado en GitHub.

Con esta base, le paso la palabra a Sergio.

**[TRANSICIÓN: pasa a Sergio]**

---

# ════════════════════════════════════════════
# BLOQUE 2 — SERGIO (≈ 2:00)
# Sección: 4. Resultados
# ════════════════════════════════════════════

**[CÁMARA: Sergio · PANTALLA: sección 4 — Resultados / gráficos]**

Gracias, Rodrigo. Soy Sergio Fernández y presento los resultados.

El hallazgo central es claro:
el análisis permitió identificar episodios críticos de MP2.5
asociados a determinadas condiciones meteorológicas.

**[PANTALLA: evolución temporal de MP2.5]**

El MP2.5 no se comporta al azar:
presenta patrones, con concentraciones notablemente más altas en meses fríos.

**[PANTALLA: promedio mensual por comuna]**

El promedio mensual por comuna confirma esa estacionalidad
y revela diferencias territoriales relevantes.

**[PANTALLA: comparación MP2.5 / MP10 + boxplots]**

Comparando MP2.5 y MP10, y apoyándonos en los boxplots,
se distinguen con claridad los periodos de mayor criticidad.

**[PANTALLA: tabla de eficiencia / benchmark]**

En lo algorítmico los resultados también son contundentes.

La búsqueda binaria localizó el umbral sobre los datos ya ordenados
con complejidad logarítmica, reduciendo de forma medible las comparaciones
frente a la búsqueda lineal.

Y la vectorización con NumPy superó ampliamente al bucle tradicional de Python
en el mismo cálculo.

En resumen: el problema no solo se resuelve;
se resuelve de forma eficiente, escalable y reproducible.

Pablo continúa con las conclusiones.

**[TRANSICIÓN: pasa a Pablo]**

---

# ════════════════════════════════════════════
# BLOQUE 3 — PABLO (≈ 2:00)
# Secciones: 5. Conclusiones · 6. Cierre
# ════════════════════════════════════════════

**[CÁMARA: Pablo · PANTALLA: sección 5 — Conclusiones]**

Gracias, Sergio. Soy Pablo Villalobos y cierro con las conclusiones.

El valor del análisis es doble.

En lo técnico, demostramos que Python automatiza todo el flujo,
que Pandas y NumPy aportan eficiencia,
y que la Programación Orientada a Objetos mejoró la mantenibilidad del código.

En lo analítico, confirmamos que el MP2.5 presenta episodios críticos
detectables y caracterizables.

**[PANTALLA: limitaciones]**

Somos transparentes con las limitaciones:
datos faltantes, estaciones con cobertura desigual
y un conjunto acotado de variables meteorológicas.

Y un punto clave: correlación no implica causalidad.
Describimos patrones, no relaciones causales directas.

**[PANTALLA: trabajo futuro]**

Como trabajo futuro proponemos un modelo de machine learning predictivo,
modelar series temporales para capturar la estacionalidad
e integrar datos climáticos adicionales.

**[PANTALLA: sección 6 — Cierre / repositorio GitHub con historial de commits]**

Para cerrar, una palabra sobre el proceso.

Este fue un trabajo colaborativo de los tres integrantes,
con evidencia trazable en GitHub:
estructura por fases, control de versiones e historial de mejoras.

El mayor aprendizaje es que la ciencia de datos no termina en el resultado:
termina cuando ese resultado se comunica de forma clara, reproducible y honesta.

Gracias por su atención.

**[PANTALLA: cierre — nombres del equipo + nombre del proyecto]**

---

## NOTAS DE PRODUCCIÓN (no se leen)
- **Tiempo estimado:** ≈ 6:30 (margen seguro dentro del rango 5–8).
- **Participan los tres** integrantes → cumple criterio de rúbrica.
- **Evidencia de colaboración:** mostrar en pantalla el historial de commits/PRs del repo durante el Bloque 3.
- Tengan a mano el notebook y los gráficos para compartir pantalla.
- Hablar mirando a cámara, sin leer de corrido.
- Ensayar una vez con cronómetro. Si superan 7:30, recortar ejemplos, no secciones.
- Grabar en Canvas Studio según indica la actividad.
- **Chequeo previo:** confirmar que la búsqueda binaria opera sobre el array ya
  ordenado por el merge sort (coherencia con la afirmación de eficiencia logarítmica).
