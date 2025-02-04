import pytest
from config_pearl import config_raw, config_parsed, config_values_only

# add tests for each toml file
# currently testing for value existence, not anything useful 
def test_raw_config():
    assert "observatory" in config_raw
    assert "telescope" in config_raw["observatory"]
    assert "fnum" in config_raw["observatory"]["telescope"]

def test_parsed_config():
    assert isinstance(config_parsed["observatory"]["telescope"]["jitter_rms"], dict)
    assert "value" in config_parsed["observatory"]["telescope"]["jitter_rms"]
    assert "unit" in config_parsed["observatory"]["telescope"]["jitter_rms"]

def test_values_only_config():
    assert isinstance(config_values_only["observatory"]["telescope"]["fnum"], float)

