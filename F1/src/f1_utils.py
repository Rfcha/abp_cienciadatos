"""
f1_utils.py - Utilidades de la Fase 1 (definición y entorno reproducible).

Este módulo concentra funciones reutilizables que evidencian modularidad
(separación de responsabilidades) en la etapa inicial del proyecto. No realiza
análisis de datos: su propósito es registrar y validar el entorno de trabajo y
verificar la calidad mínima de la definición del problema.
"""

from __future__ import annotations

import platform
import sys
from importlib import metadata


def environment_snapshot() -> dict:
    """Devuelve un registro del entorno de ejecución.

    Captura versiones de Python y de las librerías científicas relevantes para
    la Fase 1, lo que permite documentar y reproducir el ambiente de trabajo.

    Returns:
        dict: claves con la versión de Python, la plataforma y las librerías
        instaladas (pandas, numpy). Si una librería no está instalada, su valor
        es 'no instalado'.
    """
    libs = ["pandas", "numpy"]
    snapshot = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
    }
    for lib in libs:
        try:
            snapshot[lib] = metadata.version(lib)
        except metadata.PackageNotFoundError:
            snapshot[lib] = "no instalado"
    return snapshot


def validate_problem_statement(texto: str, min_palabras: int = 20) -> bool:
    """Valida que la definición de la problemática tenga sustancia mínima.

    Una buena práctica de Fase 1 es asegurar que el planteamiento del problema
    no sea un marcador de relleno. Esta función rechaza textos vacíos, textos
    que aún contienen la palabra 'COMPLETAR' y textos demasiado breves.

    Args:
        texto: enunciado de la problemática a validar.
        min_palabras: número mínimo de palabras exigido (por defecto 20).

    Returns:
        bool: True si el enunciado cumple los criterios mínimos.
    """
    if not isinstance(texto, str):
        return False
    limpio = texto.strip()
    if not limpio:
        return False
    if "COMPLETAR" in limpio.upper():
        return False
    return len(limpio.split()) >= min_palabras


def check_dependencies(requeridas: list[str]) -> dict:
    """Verifica la presencia de un conjunto de dependencias.

    Útil para confirmar, antes de ejecutar, que el entorno cuenta con las
    librerías declaradas en requirements.txt.

    Args:
        requeridas: lista de nombres de paquetes a comprobar.

    Returns:
        dict: nombre del paquete -> versión instalada o 'FALTA'.
    """
    resultado = {}
    for paquete in requeridas:
        try:
            resultado[paquete] = metadata.version(paquete)
        except metadata.PackageNotFoundError:
            resultado[paquete] = "FALTA"
    return resultado
