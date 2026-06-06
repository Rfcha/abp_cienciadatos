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


def environment_snapshot() -> dict[str, str]:
    """Devuelve un registro del entorno de ejecución.

    Captura versiones de Python y de las librerías científicas relevantes para
    la Fase 1, lo que permite documentar y reproducir el ambiente de trabajo.

    Returns:
        dict[str, str]: versión de Python, plataforma y versiones instaladas
        de pandas y numpy. Si una librería no está instalada, su valor será
        "no instalado".
    """
    libs = ["pandas", "numpy"]
    snapshot: dict[str, str] = {
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

    Rechaza textos vacíos, textos con marcadores pendientes como "COMPLETAR"
    y textos demasiado breves.

    Args:
        texto: enunciado de la problemática a validar.
        min_palabras: número mínimo de palabras exigido.

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


def check_dependencies(requeridas: list[str]) -> dict[str, str]:
    """Verifica la presencia de un conjunto de dependencias.

    Args:
        requeridas: lista de nombres de paquetes a comprobar.

    Returns:
        dict[str, str]: nombre del paquete -> versión instalada o "FALTA".
    """
    resultado: dict[str, str] = {}

    for paquete in requeridas:
        try:
            resultado[paquete] = metadata.version(paquete)
        except metadata.PackageNotFoundError:
            resultado[paquete] = "FALTA"

    return resultado
