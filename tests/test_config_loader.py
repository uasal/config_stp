import pytest
from config_pearl import ConfigLoader

loader = ConfigLoader("config_pearl/","raw",recursive=True) 
config_parsed = loader.load_configs()

def test_parsed_config():
    assert isinstance(config_parsed["observatory"]["telescope"]["jitter_rms"], dict)
    assert "value" in config_parsed["observatory"]["telescope"]["jitter_rms"]
    assert "unit" in config_parsed["observatory"]["telescope"]["jitter_rms"]

