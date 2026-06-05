"""
preprocessing.py - Pipeline de preprocesamiento de la Fase 2.

Implementa las etapas de obtención, perfilado, limpieza, transformación y
validación de un conjunto de datos de cartera de clientes. El código es
modular: cada función tiene una responsabilidad única, parámetros claros y es
verificable de forma independiente.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# Columnas según su naturaleza (facilita transformaciones diferenciadas)
NUMERICAS = ["antiguedad_meses", "monto_operacion", "dias_mora", "score_riesgo"]
CATEGORICAS = ["segmento", "region", "canal", "estado"]


def load_dataset(ruta: str | Path) -> pd.DataFrame:
    """Carga el dataset desde un archivo CSV.

    Args:
        ruta: ruta al archivo CSV de entrada.

    Returns:
        DataFrame con los datos crudos.

    Raises:
        FileNotFoundError: si la ruta no existe.
    """
    ruta = Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el dataset en: {ruta}")
    return pd.read_csv(ruta)


def profile_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un perfil resumido del DataFrame.

    Reporta, por columna, el tipo de dato, la cantidad de nulos, el porcentaje
    de nulos y el número de valores únicos. Sirve como evidencia de la
    exploración inicial y del estado del dataset antes y después de limpiar.

    Args:
        df: DataFrame a perfilar.

    Returns:
        DataFrame con una fila por columna y sus métricas de calidad.
    """
    n = len(df)
    perfil = pd.DataFrame({
        "tipo": df.dtypes.astype(str),
        "nulos": df.isna().sum(),
        "pct_nulos": (df.isna().sum() / n * 100).round(1) if n else 0,
        "unicos": df.nunique(),
    })
    return perfil


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia el dataset aplicando criterios documentados.

    Etapas:
      1. Elimina filas duplicadas exactas.
      2. Normaliza texto categórico (quita espacios y unifica capitalización).
      3. Convierte a numérico las columnas que lo requieran (casting seguro).
      4. Imputa numéricas con la mediana (robusta ante valores atípicos).
      5. Rellena categóricas no informadas con la etiqueta 'No informado'.

    Args:
        df: DataFrame crudo.

    Returns:
        DataFrame limpio, sin nulos ni duplicados.
    """
    df = df.copy()

    # 1. Duplicados exactos
    df = df.drop_duplicates().reset_index(drop=True)

    # 2. Normalización de texto categórico
    for col in CATEGORICAS:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype("string")
                .str.strip()
                .str.lower()
                .str.capitalize()
            )
            # cadenas vacías -> NA para imputar luego de forma uniforme
            df[col] = df[col].replace({"": pd.NA, "Nan": pd.NA})

    # 3. Casting seguro de numéricas (errores -> NaN)
    for col in NUMERICAS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 4. Imputación de numéricas con la mediana
    for col in NUMERICAS:
        if col in df.columns and df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())

    # 5. Categóricas no informadas
    for col in CATEGORICAS:
        if col in df.columns and df[col].isna().any():
            df[col] = df[col].fillna("No informado")

    return df


def transform_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Transforma el dataset limpio para análisis posterior.

    Etapas:
      1. Normalización MinMax de las variables numéricas (escala 0-1), para
         que variables con rangos muy distintos sean comparables.
      2. One Hot Encoding de las variables nominales.

    Args:
        df: DataFrame limpio (sin nulos).

    Returns:
        DataFrame transformado, apto para análisis o modelado.
    """
    df = df.copy()

    # 1. Normalización MinMax de numéricas (se conserva 'id' sin escalar)
    cols_norm = [c for c in NUMERICAS if c in df.columns]
    for col in cols_norm:
        rango = df[col].max() - df[col].min()
        if rango == 0:
            df[col] = 0.0  # columna constante -> evita división por cero
        else:
            df[col] = (df[col] - df[col].min()) / rango

    # 2. One Hot Encoding de nominales
    cols_ohe = [c for c in CATEGORICAS if c in df.columns]
    df = pd.get_dummies(df, columns=cols_ohe, prefix=cols_ohe)

    return df


def validate_dataset(df: pd.DataFrame) -> dict:
    """Valida la integridad del DataFrame resultante.

    Comprueba ausencia de nulos, ausencia de duplicados y que el dataset no
    esté vacío. Devuelve un diccionario de banderas para trazabilidad.

    Args:
        df: DataFrame a validar.

    Returns:
        dict con las claves 'filas', 'columnas', 'sin_nulos', 'sin_duplicados'
        y 'no_vacio'.
    """
    return {
        "filas": int(len(df)),
        "columnas": int(df.shape[1]),
        "sin_nulos": bool(df.isna().sum().sum() == 0),
        "sin_duplicados": bool(df.duplicated().sum() == 0),
        "no_vacio": bool(len(df) > 0),
    }


def run_pipeline(ruta_entrada: str | Path, ruta_salida: str | Path) -> tuple:
    """Ejecuta el pipeline completo de extremo a extremo.

    Carga, limpia, transforma, valida y persiste el dataset procesado.

    Args:
        ruta_entrada: ruta del CSV crudo.
        ruta_salida: ruta donde se guardará el CSV procesado.

    Returns:
        tuple: (df_limpio, df_transformado, dict_validacion).
    """
    ruta_salida = Path(ruta_salida)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    df_raw = load_dataset(ruta_entrada)
    df_clean = clean_dataset(df_raw)
    df_transformed = transform_dataset(df_clean)
    validacion = validate_dataset(df_transformed)

    df_transformed.to_csv(ruta_salida, index=False, encoding="utf-8")
    return df_clean, df_transformed, validacion
