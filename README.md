## Overview
`config_pearl` is a Python package that provides access to observatory, instrument, and astrophysics configuration data stored in TOML format. Currently there are 3 data formats this package makes available, "raw" which returns a dictionary of strings as whatever format they're stored in, "parsed" which reads .toml files and separates out 'value' and 'unit', and "unitless" which parses the input string and removes any units. See examples below for how to grab each format. 

The parser currently searches
* config_pearl/config/

for .toml files and creates a dict where the first value is the name of the file, recursively adding values based on the .toml format hierarchy. Directories are hard-coded in the package, so this will need to be generalized if the tool will be viable for use by other repositories.  

## Installation Instructions

### **1. Clone the Repository**
To get started, clone this repository using:
```sh
git clone git@github.com:uasal/config_pearl.git
cd config_pearl
```

### **2. Install the Package**
Once inside the project directory, install the package using:
```sh
pip install .
```

## Usage and Verifying the Installation
Once installed, you can import `config_raw` `config_parsed` or `config_values_only` as shown below. If unable to import, the pip installation has failed or you are in a different environment. You may have cloned a bad commit state, so verify the commit hash matches the latest 'stable' commit reported in the 'Test Results' section. An official release version will be added later. 

### Raw
```python
from config_pearl import ConfigLoader

loader = ConfigLoader("config_pearl/config_pearl/config","raw",recursive=True) #relative path from where you run the tool
config_parsed = loader.load_configs()
print(config_parsed["observatory"]["telescope"]["jitter_rms"])
```

## Troubleshooting
If you encounter issues, try the following:
- Ensure you are running Python 3.12
- Check that `pip list | grep config_pearl` confirms the package is installed
- Uninstall and reinstall using:
  ```sh
  pip uninstall config_pearl
  pip install .
  ```

If you'd like to print the whole dictionary in all 3 formats for a sanity check, you can borrow the following 
```python
from config_pearl import ConfigLoader
import json

config_raw = ConfigLoader("config_pearl/config_pearl/config","raw").load_configs() 
config_parsed = ConfigLoader("config_pearl/config_pearl/config","parsed").load_configs()
config_unitless = ConfigLoader("config_pearl/config_pearl/config","unitless").load_configs()

def print_dict(title, data):
    """Print pearl dictionary for all 3 formats -- json formatted!"""
    print(json.dumps(data, indent=4, sort_keys=True))

if __name__ == "__main__":
    print("\n===========   {raw}   ===========")
    print_dict("Raw Astropy TOML Data", config_raw)
    print("\n===========  {parsed}  ===========")
    print_dict("Parsed TOML Data (Value + Unit)", config_parsed)
    print("\n=========== {unitless} ===========")
    print_dict("Values-Only TOML Data", config_unitless)
```

---
