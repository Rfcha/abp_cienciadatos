"""Pipeline F2: obtencion, limpieza, transformacion y validacion de datos."""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

NUMERIC_COLUMNS = ["antiguedad_meses", "monto_operacion", "dias_mora", "score_riesgo"]
CATEGORICAL_COLUMNS = ["segmento", "region", "canal", "estado"]


def load_dataset(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset no encontrado: {path}")
    return pd.read_csv(path)


def profile_dataset(df: pd.DataFrame) -> pd.DataFrame:
    profile = pd.DataFrame({
        "tipo": df.dtypes.astype(str),
        "nulos": df.isna().sum(),
        "nulos_pct": (df.isna().mean() * 100).round(2),
        "unicos": df.nunique(dropna=True),
    })
    return profile


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    clean = df.copy()
    clean = clean.drop_duplicates()

    for col in NUMERIC_COLUMNS:
        if col in clean.columns:
            clean[col] = pd.to_numeric(clean[col], errors="coerce")
            clean[col] = clean[col].fillna(clean[col].median())

    for col in CATEGORICAL_COLUMNS:
        if col in clean.columns:
            clean[col] = clean[col].astype("string").str.strip()
            clean[col] = clean[col].fillna("No informado")

    return clean


def transform_dataset(df: pd.DataFrame) -> pd.DataFrame:
    transformed = df.copy()
    scaler_cols = [c for c in ["antiguedad_meses", "monto_operacion", "dias_mora", "score_riesgo"] if c in transformed.columns]
    if scaler_cols:
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(transformed[scaler_cols])
        for idx, col in enumerate(scaler_cols):
            transformed[f"{col}_norm"] = scaled[:, idx]

    nominal_cols = [c for c in ["segmento", "region", "canal", "estado"] if c in transformed.columns]
    if nominal_cols:
        transformed = pd.get_dummies(transformed, columns=nominal_cols, drop_first=False, dtype=int)

    return transformed


def validate_dataset(df: pd.DataFrame) -> dict:
    return {
        "filas": int(df.shape[0]),
        "columnas": int(df.shape[1]),
        "duplicados": int(df.duplicated().sum()),
        "nulos_totales": int(df.isna().sum().sum()),
        "sin_nulos": bool(df.isna().sum().sum() == 0),
        "sin_duplicados": bool(df.duplicated().sum() == 0),
    }


def run_pipeline(input_path: str | Path, output_path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    raw = load_dataset(input_path)
    clean = clean_dataset(raw)
    transformed = transform_dataset(clean)
    validation = validate_dataset(transformed)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    transformed.to_csv(output_path, index=False)
    return clean, transformed, validation