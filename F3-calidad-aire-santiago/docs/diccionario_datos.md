# Diccionario de datos — calidad del aire RM

Dataset horario de calidad del aire para 11 estaciones de la Región
Metropolitana, periodo 2022-2023 (192.720 registros).

## Variables

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| `fecha` | texto | dd-mm-aaaa HH:MM | Fecha y hora del registro |
| `estacion` | texto | — | Nombre de la estación de monitoreo |
| `comuna` | texto | — | Comuna donde se ubica la estación |
| `MP2.5` | numérico | µg/m³ | Material particulado fino (variable objetivo) |
| `MP10` | numérico | µg/m³ | Material particulado respirable |
| `temperatura` | numérico | °C | Temperatura del aire |
| `humedad` | numérico | % | Humedad relativa |
| `presion` | numérico | hPa | Presión atmosférica |
| `viento` | numérico | m/s | Velocidad del viento |
| `radiacion` | numérico | W/m² | Radiación solar |
| `inversion_termica` | binaria | 0/1 | Presencia de inversión térmica |
| `dia_semana` | entero | 0-6 | Día de la semana (0=lunes) |
| `es_finde` | binaria | 0/1 | 1 si es sábado o domingo |
| `es_festivo` | binaria | 0/1 | 1 si es feriado en Chile |

## Formato del archivo

- Separador de columnas: punto y coma (`;`)
- Separador decimal: coma (`,`)
- Codificación: latin-1

Lectura en pandas:
```python
df = pd.read_csv('../data/raw/sinca_santiago.csv',
                 sep=';', decimal=',', encoding='latin-1')
```

## Nota sobre el origen de los datos

Este es un **dataset sintético de demostración** construido para reproducir
relaciones físicas documentadas de la contaminación atmosférica en Santiago
(inversión térmica invernal, efecto de ventilación del viento, ciclo diario
asociado a transporte y calefacción a leña, y menor actividad en fines de
semana y festivos). Permite desarrollar y validar el flujo de análisis
reproducible. Para conclusiones definitivas deben utilizarse datos reales
descargados del SINCA (https://sinca.mma.gob.cl).

## Referencia

Ministerio del Medio Ambiente. (2024). *Sistema de Información Nacional de
Calidad del Aire (SINCA)*. https://sinca.mma.gob.cl
