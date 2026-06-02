"""Utilidades comunes del proyecto ABP."""
from pathlib import Path
import pandas as pd


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_csv(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")
    return pd.read_csv(path)


def basic_profile(df: pd.DataFrame) -> dict:
    return {
        "filas": int(df.shape[0]),
        "columnas": int(df.shape[1]),
        "duplicados": int(df.duplicated().sum()),
        "nulos_totales": int(df.isna().sum().sum()),
    }