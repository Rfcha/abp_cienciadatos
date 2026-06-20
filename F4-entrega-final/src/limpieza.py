"""
Módulo de Preprocesamiento Orientado a Objetos — Proyecto F3 Calidad del Aire
Magíster en Ciencia de Datos e Inteligencia Artificial, UNAB
Autores: Rodrigo Chinchón, Pablo Villalobos, Sergio Fernández
"""

import os
import pandas as pd


class PreprocesadorAire:
    """Clase responsable de la ingesta y consistencia del linaje de datos."""

    def __init__(self, ruta_csv: str):
        """
        Inicializa el preprocesador validando la existencia de la fuente.
        
        Cita: McKinney (2022) para la manipulación estructurada de dataframes.
        """
        if not os.path.exists(ruta_csv):
            raise FileNotFoundError(f"No se encontró el dataset en: {ruta_csv}")
        self.ruta_csv = ruta_csv

    def ejecutar_pipeline(self) -> pd.DataFrame:
        """
        Orquesta el flujo reproducible: Carga -> Limpieza de nulos y tipos.
        
        Returns:
            pd.DataFrame: Conjunto de datos limpio y listo para el modelado.
        """
        # Carga con especificaciones de formato SINCA (Ministerio del Medio Ambiente, 2024)
        df = pd.read_csv(
            self.ruta_csv, sep=";", decimal=",", encoding="latin-1"
        )

        # Definición de columnas mandatorias para análisis meteorológico y ambiental
        columnas_clave = ["MP2.5", "MP10", "temperatura", "humedad", "viento"]

        # Filtrado estricto de registros incompletos
        df_limpio = df.dropna(subset=[c for c in columnas_clave if c in df.columns]).copy()

        return df_limpio