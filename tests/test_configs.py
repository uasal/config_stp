import pytest
import config_stp
from pathlib import Path
import astropy.units as u

from utils_config import ConfigLoader

CONFIGS_PATH = Path(config_stp.__file__).parent / "configs"

def test_load_configs_valid():
    """
    Test that all TOML files in the package's 'configs' directory are valid.
    If any file is malformed, ConfigLoader.load_configs() raises an error, causing the test to fail.
    """
    loader = ConfigLoader(str(CONFIGS_PATH), mode="parsed", recursive=False)
    try:
        configs = loader.load_configs()
    except Exception as e:
        pytest.fail(f"Failed to load TOML configs: {e}")
    assert configs, "No configuration files were loaded."

def test_astropy_units():
    """
    Test that all unit strings in the parsed configuration files ("parsed" format) are valid Astropy units.
    uses the ConfigLoader class + validate_astropy() method to parse configs installed in this package
    and then return either [] for no errors (passing assert), or a list containing information on each violation
    """
    errors = config_stp.load_config_values("parsed", return_loader=True).validate_astropy()
    assert errors == [], "Invalid astropy units found:\n" + "\n".join(errors)
