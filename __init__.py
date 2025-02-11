from .config_loader import load_config_values

CONFIG_VALUES = None

def get_config():
    global CONFIG_VALUES
    if CONFIG_VALUES is None:
        CONFIG_VALUES = load_config_values()
    return CONFIG_VALUES

