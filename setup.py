from setuptools import setup, find_packages

setup(
    name="config_pearl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["toml"],
    include_package_data=True,
    package_data={"config_pearl": ["config/observatory/*.toml"]},
)
 
