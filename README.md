# config_pearl

## Overview
`config_pearl` is a Python package that provides access to observatory, instrument, and astrophysics configuration data stored in TOML format. It allows easiy retrieval of parameters via a dict. This repo may contain .csv, .fits, and other data formats later on to be ingested by tools_pearl

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

## Verifying the Installation
After installation, you can test that the package works correctly by running the following Python snippet:

```python
from config_pearl import observatory_config

print(observatory_config["telescope"]["fnum"])  # Output: 15.0
print(observatory_config["WCC"]["FOV_w"])       # Output: '13.75arcminute'
```

other dicts available for import include
* esc_config
* ifs_config
* universe_config

## Usage
Once installed, you can import `observatory_config` or any of the other dicts anywhere in your Python code to access the configuration data.

## Troubleshooting
If you encounter issues, try the following:
- Ensure you are running Python 3.x
- Check that `pip list | grep config_pearl` confirms the package is installed
- Uninstall and reinstall using:
  ```sh
  pip uninstall config_pearl
  pip install .
  ```


---

 
