# config_stp

Space Telescope Pathfinder repository for support data and configuration management as an installable python package 
 
The [main](https://github.com/uasal/config_stp/tree/main) branch of this repo is under STP change control. The [develop](https://github.com/uasal/config_stp/tree/develop) branch is currently the default to enable rapid development of systems engineering budgets but the default will be changed to main once baseline observatory design is frozen. Changes to main require code owner approval, changes to the develop branch require approval of two other team members.

Details on the change control process are found in the [coronograph design documentation repository](https://github.com/uasal/spacecoron_design_docs)

This repository contains reference data for the observatory and telescope.
The data in the repository is intended to encapsulate all parameters which represent the high-level system and are to be identical when called by the the various tools/simulators.
This includes details of the telescope optical system, such as coatings and sensors, and observatory properties such as slew times.
A synthetic dataset regarding the timeseries for the wavefront error due the thermal effects is also available.

The parameters for each subsystem are found in the `configs` directory.
A description of how configurations are used in UASAL software, users can find an example notebook in the `docs` directory of the  [config_project_template](https://github.com/uasal/config_project_template) repository. 
The example demonstrates how to load the TOML parameter files in a Python script.
TOML files are human readible configuration files that can be read with a range of parsers https://github.com/toml-lang/toml/wiki

## Dependencies
config_stp is dependent on [utils_config](https://github.com/uasal/utils_config) but will be automatically installed. 

## Installation
ssh keys are required for the pip-based install. Verify you have ssh keys installed in GitHub, or check out this [ssh key tutorial](https://github.com/uasal/lab_documents/blob/main/ssh_key_tutorial.md)

### Pip-based install
```sh
pip install git+ssh://git@github.com/uasal/config_stp.git
```

### Installed via cloning
```sh
git clone git@github.com:uasal/config_stp.git
cd config_stp
pip install .
```

## Usage
config_stp makes usage of the ConfigLoader class (as *config_loader*) from utils_config via the `load_config_values` method, which accepts 'raw' 'parsed' or 'unitless' as an argument, returning a dictionary after parsing the 'configs' directory for .toml filies
```python
import config_stp
data = config_stp.load_config_values()
print(data["observatory"]["pointing"]["jitter_rms"])
```

load_config_values() has a default argument of 'raw' or alternatively pass in one of the three viable arguments for how values should be presented: 
- `load_config_values('unitless')` -> 0.01
- `load_config_values('parsed')` -> {'value': 0.01, 'unit': 'arcsecond'}
- `load_config_values('raw')` -> 10e-3arcsecond

For importing data and keeping code consistent across installs, config_stp will return the path to support_data with `get_data_path()`
```python
import config_stp
data_path = config_stp.get_data_path()
print(data_path)
```

### Version Reporting

For the reporting configuration versions in analyses (to aid in repeatability), the method `check_imports_and_versions` is available inside [utils_config](https://github.com/uasal/utils_config) that generates a nice summary. 

## Astropy Unit Validation

All .toml config values should have a valid astropy unit if any units are defined. If no unit is included, the value is assumed to be unitless. A GitHub CI will automatically run a test on push to validate astropy units in the configs, reporting any issues with non-conforming astropy units. If you'd like to perform validation locally, you may run `pytest tests/test_configs.py` from the root directory of the repo. Alternatively in your python environment you may run the following snippit:
```python
import config_stp
config_stp.load_config_values("parsed", return_loader=True).validate_astropy()
```
Which will return 'True' if every unit is a valid astropy unit, or a list containing every invalid unit. If you would like to use a custom u
nit, click [here](https://docs.astropy.org/en/stable/units/combining_and_defining.html#defining-units) for how to define that as a custom unit in Astropy. 

## Git large file storage (LFS)

This repository makes use of the git large file storage for files listed in the `.gitattributes` file.
Accessing these files will require users having (Git Large File Storage (LFS))[https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage] installed on their local machine.

If you have Git LFS installed, then the large files will be pulled by default.
This can be disabled in your gitconfig, as described (at this link)[https://stackoverflow.com/questions/42019529/how-to-clone-pull-a-git-repository-ignoring-lfs].
