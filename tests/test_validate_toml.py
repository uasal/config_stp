import pytest
import os
import toml
from pathlib import Path

# Get absolute project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define required config directories (adjusted for absolute paths)
CONFIG_DIRECTORIES = [
    PROJECT_ROOT / "config_pearl" / "config"
    # add new directories here that are mandatory
]

DATA_DIRECTORIES = [
    PROJECT_ROOT / "config_pearl" / "data" 
]

@pytest.mark.parametrize("folder", CONFIG_DIRECTORIES)
def test_folders_exist(folder):
    assert folder.is_dir(), f"Missing required directory: {folder}"

@pytest.mark.parametrize("folder", CONFIG_DIRECTORIES)
def test_toml_files_valid(folder):
    toml_files = list(folder.glob("*.toml"))

    assert toml_files, f"No TOML files found in {folder}"

    for toml_file in toml_files:
        try:
            with open(toml_file, "r") as f:
                toml.load(f)  # Attempt to parse the TOML file
        except Exception as e:
            pytest.fail(f"TOML parsing failed for {toml_file}: {e}")

