import importlib.metadata
from config_pearl import load_config_values, get_data_path

__version__ = importlib.metadata.version(__package__ or "config_pearl")

__all__ = ["load_config_values", "get_data_path"]
