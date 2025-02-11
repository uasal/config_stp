from utils_config import ConfigLoader
import os

def load_config_values(value="raw"):
    config_dir = os.path.join(os.path.dirname(__file__), "configs")
    loader = ConfigLoader(config_dir, value, recursive=True)
    return loader.load_configs()
