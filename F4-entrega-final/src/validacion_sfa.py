"""
validacion_sfa.py

Módulo complementario de validación para la Fase 3 del proyecto
Calidad del Aire - Santiago.

Este archivo incorpora funciones simples para revisar la consistencia
del dataset limpio antes de utilizarlo en análisis exploratorio,
visualizaciones o algoritmos posteriores.

Autor: Sergio Fernández Almonacid
Fase: F3
"""

from pathlib import Path
import pandas as pd


def cargar_dataset_limpio(ruta_csv: str | Path) -> pd.DataFrame:
    """
    Carga el dataset limpio de F3 desde una ruta CSV.

    Parameters
    ----------
    ruta_csv : str | Path
        Ruta del archivo CSV limpio.

    Returns
    -------
    pd.DataFrame
        Dataset cargado como DataFrame de pandas.

    Raises
    ------
    FileNotFoundError
        Si el archivo no existe.
    ValueError
        Si el archivo existe, pero no contiene registros.
    """
    ruta_csv = Path(ruta_csv)

    if not ruta_csv.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    df = pd.read_csv(ruta_csv)

    if df.empty:
        raise ValueError("El dataset está vacío. No es posible validar un archivo sin registros.")

    return df


def resumen_calidad_datos(df: pd.DataFrame) -> dict:
    """
    Genera un resumen básico de calidad del dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset a validar.

    Returns
    -------
    dict
        Diccionario con filas, columnas, nulos, duplicados y tipos de datos.
    """
    resumen = {
        "filas": df.shape[0],
        "columnas": df.shape[1],
        "nulos_totales": int(df.isna().sum().sum()),
        "duplicados": int(df.duplicated().sum()),
        "columnas_con_nulos": df.columns[df.isna().any()].tolist(),
        "tipos_datos": df.dtypes.astype(str).to_dict(),
    }

    return resumen


def validar_dataset_para_f3(df: pd.DataFrame) -> dict:
    """
    Valida condiciones mínimas del dataset limpio para análisis F3.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio de F3.

    Returns
    -------
    dict
        Resultado de validación con banderas booleanas y observaciones.
    """
    resumen = resumen_calidad_datos(df)

    resultado = {
        "filas_validas": resumen["filas"] > 0,
        "columnas_validas": resumen["columnas"] > 0,
        "sin_duplicados": resumen["duplicados"] == 0,
        "sin_nulos": resumen["nulos_totales"] == 0,
        "apto_para_analisis": (
            resumen["filas"] > 0
            and resumen["columnas"] > 0
            and resumen["duplicados"] == 0
            and resumen["nulos_totales"] == 0
        ),
        "resumen": resumen,
    }

    return resultado


if __name__ == "__main__":
    ruta = Path(__file__).resolve().parents[1] / "data" / "processed" / "sinca_limpio.csv"

    dataset = cargar_dataset_limpio(ruta)
    validacion = validar_dataset_para_f3(dataset)

    print("Resumen de validación F3 - SFA")
    print("--------------------------------")
    print(f"Filas: {validacion['resumen']['filas']}")
    print(f"Columnas: {validacion['resumen']['columnas']}")
    print(f"Nulos totales: {validacion['resumen']['nulos_totales']}")
    print(f"Duplicados: {validacion['resumen']['duplicados']}")
    print(f"Apto para análisis: {validacion['apto_para_analisis']}")