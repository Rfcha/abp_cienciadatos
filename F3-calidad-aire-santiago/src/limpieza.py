"""Funciones de limpieza y carga de datos del SINCA."""

import pandas as pd


def cargar_datos(ruta: str) -> pd.DataFrame:
    """Carga un CSV del SINCA en un DataFrame."""
    return pd.read_csv(ruta)


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas con valores nulos en las columnas clave."""
    columnas = ["MP2.5", "MP10", "temperatura", "humedad", "viento"]
    return df.dropna(subset=[c for c in columnas if c in df.columns])
