import os
from pathlib import Path
from utils_config import ConfigLoader

def load_config_values(value="raw"):
    package_root = Path(__file__).parent.resolve()
    config_dir = package_root / "configs"

    if not config_dir.exists():
        raise FileNotFoundError(f"Config directory not found: {config_dir}")

    loader = ConfigLoader(str(config_dir), value, recursive=True)
    return loader.load_configs()
