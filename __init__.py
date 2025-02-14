import importlib.metadata
from config_loader import load_config_values

__version__ = importlib.metadata.version(__package__ or "config_pearl")

__all__ = ["load_config_values"]
