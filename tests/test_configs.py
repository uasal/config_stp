import pytest
import config_stp
from pathlib import Path
import astropy.units as u

from utils_config import ConfigLoader

# Use the package's own path to locate the configs directory
CONFIGS_PATH = Path(config_stp.__file__).parent / "configs"

def test_load_configs_valid():
    """
    Test that all TOML files in the package's 'configs' directory are valid.
    If any file is malformed, ConfigLoader.load_configs() will raise an error, causing the test to fail.
    """
    loader = ConfigLoader(str(CONFIGS_PATH), mode="parsed", recursive=False)
    try:
        configs = loader.load_configs()
    except Exception as e:
        pytest.fail(f"Failed to load TOML configs: {e}")
    assert configs, "No configuration files were loaded."

def test_units_valid():
    """
    Test that all unit strings in the parsed configuration files are valid Astropy units.
    The test recursively checks the configuration dictionary, and if a dictionary with 'value'
    and 'unit' keys is found, it attempts to create an Astropy Unit from the 'unit' string.
    """
    loader = ConfigLoader(str(CONFIGS_PATH), mode="parsed", recursive=False)
    try:
        configs = loader.load_configs()
    except Exception as e:
        pytest.fail(f"Failed to load TOML configs: {e}")

    def check_units(data):
        if isinstance(data, dict):
            # Check 'unit' in 'value' 'unit' pair. Relies on ConfigLoader parsing units out correctly
            if "value" in data and "unit" in data:
                unit_str = data["unit"]
                try:
                    u.Unit(unit_str)  # Raise an exception if the unit is invalid
                except Exception as e:
                    pytest.fail(f"Invalid unit '{unit_str}': {e}")
            else:
                for value in data.values():
                    check_units(value)
        elif isinstance(data, list):
            for item in data:
                check_units(item)
        # Ignore any other types

    for config in configs.values():
        check_units(config)

