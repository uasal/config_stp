import toml
import re
from pathlib import Path

class ConfigLoader:
    """Class to load and process configuration files."""

    def __init__(self, base_path: Path):
        self.base_path = base_path

    def load_config(self, filename: str, parse_units: bool = False, values_only: bool = False):
        """
        Load a TOML configuration file.
        
        :param filename: Name of the TOML file to load.
        :param parse_units: If True, parses values into {"value": float, "unit": str}.
        :param values_only: If True, extracts only numerical values, removing units.
        :return: Dictionary containing the loaded configuration.
        """
        filepath = self.base_path / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Config file {filename} not found in {self.base_path}")

        raw_config = toml.load(filepath)
        if parse_units:
            return self._process_config(raw_config, values_only)
        return raw_config  # Return as-is if no parsing is requested

    def _process_config(self, config, values_only: bool):
        """Recursively process configuration dictionary to parse values and units."""
        if isinstance(config, dict):
            return {key: self._process_config(value, values_only) for key, value in config.items()}
        elif isinstance(config, str):
            return self._parse_value_with_units(config, values_only)
        else:
            return config  # Keep numbers, booleans, and other types unchanged

    def _parse_value_with_units(self, value, values_only: bool):
        """
        Extract numerical value and unit from a string.
        Example:
        - '10e-3arcsecond' → {'value': 1.0e-2, 'unit': 'arcsecond'}
        - '0.024Kelvin/hour' → {'value': 0.024, 'unit': 'Kelvin/hour'}
        """
        match = re.match(r"([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)([a-zA-Z/%µ]+$)", value.strip())
        if match:
            num, unit = match.groups()
            return float(num) if values_only else {"value": float(num), "unit": unit} if unit else float(num)
        return value  # Return as-is if it doesn't match the expected format

# Instantiate loader to access configurations
config_path = Path(__file__).parent / "config/observatory"
config_loader = ConfigLoader(config_path)

# Load observatory config in three modes
observatory_config_raw = config_loader.load_config("observatory.toml", parse_units=False)
observatory_config_parsed = config_loader.load_config("observatory.toml", parse_units=True)
observatory_config_values_only = config_loader.load_config("observatory.toml", parse_units=True, values_only=True)

