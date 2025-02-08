import pathlib
import unittest
import tomlkit
from config_pearl import tests
import astropy


class TestConfigs(TestCase):
    "Tests for psd_utils."

    def test_tomls(self):
        # Go and read in each config file and check for syntax errors
        files = *.toml
        tests.syntax(files)
        # Also check astropy unit compatibility
        tests.astropy_units(files)
        pass


    