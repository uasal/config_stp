import toml
from pathlib import Path

class ConfigLoader:
    """Class to load and provide access to configuration files."""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def load_config(self, filename: str):
        """Load a TOML configuration file from the config directory."""
        filepath = self.base_path / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Config file {filename} not found in {self.base_path}")
        return toml.load(filepath)

# Instantiate loader to access configurations
config_path = Path(__file__).parent / "config/observatory"
config_loader = ConfigLoader(config_path)

# Load observatory config
observatory_config = config_loader.load_config("observatory.toml")

