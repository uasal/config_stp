import toml
import pytest
from pathlib import Path

# Define directories containing TOML files
CONFIG_DIRECTORIES = [
    Path(__file__).parent.parent / "config/observatory",
    Path(__file__).parent.parent / "config/instruments"  # add more directories as needed
]

@pytest.mark.parametrize("toml_file", [f for d in CONFIG_DIRECTORIES for f in d.glob("*.toml")])
def test_toml_format(toml_file):
    """Ensure each TOML file is correctly formatted and can be parsed."""
    try:
        with open(toml_file, "r") as f:
            toml.load(f)
    except toml.TomlDecodeError as e:
        pytest.fail(f"TOML parsing failed for {toml_file}: {e}")
