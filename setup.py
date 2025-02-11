#from setuptools import setup 

#setup()

from setuptools import setup, find_packages

setup(
    name="config_pearl",
    version="0.1.0",
    packages=["config_pearl"],
    package_dir={'config_pearl': '.',},
    install_requires=["utils_config"],
    include_package_data=True,
    package_data={"": ["configs/*.toml"]},
)

