import pytest
from config_pearl import config_raw, config_parsed, config_values_only

# add tests for each toml file

def test_raw_config():
    """Ensure raw configuration is loaded without errors. Validate certain values exist"""
    assert "observatory" in config_raw
    assert "telescope" in config_raw["observatory"]
    assert "fnum" in config_raw["observatory"]["telescope"]

def test_parsed_config():
    """Ensure parsed configuration correctly separates values and units."""
    assert isinstance(config_parsed["observatory"]["telescope"]["jitter_rms"], dict)
    assert "value" in config_parsed["observatory"]["telescope"]["jitter_rms"]
    assert "unit" in config_parsed["observatory"]["telescope"]["jitter_rms"]

def test_values_only_config():
    """Ensure values-only configuration removes units and keeps only numbers."""
    assert isinstance(config_values_only["observatory"]["telescope"]["fnum"], float)

