import toml
import re
from pathlib import Path

class ConfigLoader:

    def __init__(self, base_dirs):
        self.base_dirs = [Path(d) for d in base_dirs]

    def load_all_configs(self, parse_units: bool = False, values_only: bool = False):
        """
        Load all TOML files from specified directories into a global dictionary.
        
        :param parse_units: If True, parses values into {"value": float, "unit": str}.
        :param values_only: If True, extracts only numerical values, removing units.
        :return: Dictionary containing all loaded configurations.
        """
        config_data = {}
        for base_dir in self.base_dirs:
            if not base_dir.exists():
                raise FileNotFoundError(f"Config directory {base_dir} not found.")

            for toml_file in base_dir.glob("*.toml"):
                file_name = toml_file.stem  # Use filename (without .toml) as dictionary key
                config_data[file_name] = self._process_config(toml.load(toml_file), parse_units, values_only)

        return config_data

    def _process_config(self, config, parse_units: bool, values_only: bool):
        """Recursively process configuration dictionary to parse values and units."""
        if isinstance(config, dict):
            return {key: self._process_config(value, parse_units, values_only) for key, value in config.items()}
        elif isinstance(config, str):
            return self._parse_value_with_units(config, values_only) if parse_units else config
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

config_directories = [
    Path(__file__).parent / "config" / "observatory",
    Path(__file__).parent / "config" / "instruments"
]

config_loader = ConfigLoader(config_directories)

# 3 different modes loaded into objects from 'load_all_configs'
config_raw = config_loader.load_all_configs(parse_units=False)
config_parsed = config_loader.load_all_configs(parse_units=True)
config_values_only = config_loader.load_all_configs(parse_units=True, values_only=True)

