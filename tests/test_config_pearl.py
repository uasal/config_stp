import pytest
import importlib.metadata
import config_pearl
import toml
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
CONFIGS_PATH = PROJECT_ROOT / "configs"

def test_version_consistency():
    """Ensure __version__ and importlib.metadata.version report the same value."""
    package_version = importlib.metadata.version("config_pearl")
    module_version = config_pearl.__version__

    if package_version != module_version:
        pytest.warns(UserWarning, f"Version mismatch: __version__={module_version}, metadata.version={package_version}")

    assert module_version == package_version, f"Version mismatch: __version__={module_version}, metadata.version={package_version}. Verify package is up-to-date."


@pytest.mark.parametrize("toml_file", CONFIGS_PATH.glob("*.toml"))
def test_toml_files_valid(toml_file):
    """Ensure all .toml files in configs/ are a valid TOML format."""
    try:
        with open(toml_file, "r") as f:
            toml.load(f)
    except Exception as e:
        pytest.fail(f"TOML parsing failed for {toml_file}: {e}")

