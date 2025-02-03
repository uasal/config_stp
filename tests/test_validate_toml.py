import pytest
import os
import toml
from pathlib import Path

# Get absolute project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define required config directories (adjusted for absolute paths)
CONFIG_DIRECTORIES = [
    PROJECT_ROOT / "config_pearl" / "config" / "observatory",
    PROJECT_ROOT / "config_pearl" / "config" / "instruments"
    # add new directories here that are mandatory
]

#add new tests for files if we're forcing certain config files to be part of the package?

@pytest.mark.parametrize("folder", CONFIG_DIRECTORIES)
def test_folders_exist(folder):
    """Ensure required config directories exist."""
    assert folder.is_dir(), f"Missing required directory: {folder}"

@pytest.mark.parametrize("folder", CONFIG_DIRECTORIES)
def test_toml_files_valid(folder):
    """Ensure TOML files inside each folder are correctly formatted."""
    toml_files = list(folder.glob("*.toml"))

    assert toml_files, f"No TOML files found in {folder}"

    for toml_file in toml_files:
        try:
            with open(toml_file, "r") as f:
                toml.load(f)  # Attempt to parse the TOML file
        except Exception as e:
            pytest.fail(f"TOML parsing failed for {toml_file}: {e}")

