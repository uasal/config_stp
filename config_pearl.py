import os
import importlib.metadata
from pathlib import Path
from utils_config import ConfigLoader

# Define module version safely
try:
    __version__ = importlib.metadata.version("config_pearl")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

def load_config_values(value="raw"):
    """Loads configuration values from the 'configs' directory."""
    config_dir = os.path.join(os.path.dirname(__file__), "configs")
    loader = ConfigLoader(config_dir, value, recursive=True)
    return loader.load_configs()

def get_data_path():
    """Returns the full absolute path to the installed 'support_data' directory."""
    package_root = Path(__file__).parent.resolve()  # ✅ Get the absolute path of this package
    data_path = package_root / "support_data"  # ✅ Find 'support_data/' in the same directory

    if not data_path.exists():
        raise FileNotFoundError(f"Support data directory not found: {data_path}")

    return str(data_path)

# Expose functions so they can be accessed via `config_pearl.load_config_values()` and `config_pearl.get_data_path()`
__all__ = ["load_config_values", "get_data_path"]

