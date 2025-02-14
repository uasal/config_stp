import os
import importlib.metadata
from pathlib import Path
from utils_config import ConfigLoader

try:
    __version__ = importlib.metadata.version("config_pearl")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

def load_config_values(value="raw"):
    config_dir = os.path.join(os.path.dirname(__file__), "configs")
    loader = ConfigLoader(config_dir, value, recursive=True)
    return loader.load_configs()

def get_data_path():
    package_root = Path(__file__).parent.resolve()
    data_path = package_root / "support_data"

    if not data_path.exists():
        raise FileNotFoundError(f"Support data directory not found: {data_path}")

    return str(data_path)

__all__ = ["load_config_values", "get_data_path"]

