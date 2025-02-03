import pytest
import os
import toml
from pathlib import Path

# Define required config directories
CONFIG_DIRECTORIES = [
    "config/observatory",
    "config/instruments"
]

@pytest.mark.parametrize("folder", CONFIG_DIRECTORIES)
def test_folders_exist(folder):
    """Ensure required config directories exist."""
    assert os.path.isdir(folder), f"Missing required directory: {folder}"

@pytest.mark.parametrize("folder", CONFIG_DIRECTORIES)
def test_toml_files_valid(folder):
    """Ensure TOML files inside each folder are correctly formatted."""
    folder_path = Path(folder)
    toml_files = list(folder_path.glob("*.toml"))

    assert toml_files, f"No TOML files found in {folder}"

    for toml_file in toml_files:
        try:
            with open(toml_file, "r") as f:
                toml.load(f)  # Attempt to parse the TOML file
        except Exception as e:
            pytest.fail(f"TOML parsing failed for {toml_file}: {e}")

