"""Funciones utilitarias base - Fase 1."""
import pandas as pd


def cargar_dataset(ruta: str) -> pd.DataFrame:
    """Carga un dataset CSV y devuelve un DataFrame."""
    return pd.read_csv(ruta)


def resumen_basico(df: pd.DataFrame) -> dict:
    """Devuelve un resumen inicial del DataFrame (filas, columnas, nulos)."""
    return {
        "filas": int(df.shape[0]),
        "columnas": int(df.shape[1]),
        "nulos_totales": int(df.isnull().sum().sum()),
    }