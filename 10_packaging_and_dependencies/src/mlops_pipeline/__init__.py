"""
MLOps Pipeline Package
Modern Python package structure for ML workflows
"""

__version__ = "1.2.3"
__author__ = "MLOps Team"

from .models import ModelTrainer
from .data import DataProcessor

__all__ = ["ModelTrainer", "DataProcessor"]