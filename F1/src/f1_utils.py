"""Funciones base para Fase 1: definicion, trazabilidad y entorno."""
import sys
import platform
import pandas as pd
import numpy as np


def environment_snapshot() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "pandas": pd.__version__,
        "numpy": np.__version__,
    }


def validate_problem_statement(text: str) -> bool:
    return isinstance(text, str) and len(text.strip()) >= 40