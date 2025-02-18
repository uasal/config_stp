import importlib.metadata
from .config_loader import load_config_values
from pathlib import Path

__version__ = importlib.metadata.version(__package__ or "config_stp")

def get_data_path():
    package_root = Path(__file__).parent.resolve()
    data_path = package_root / "support_data"

    if not data_path.exists():
        raise FileNotFoundError(f"Support data directory not found: {data_path}")

    return str(data_path)

__all__ = ["load_config_values", "get_data_path", "__version__"]

