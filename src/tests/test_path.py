"""Tests that pass on GitHub actions or pytest 
iff project contains necessary files in same path."""
import os


def test_data():
    """Passes if user's working directory has a data folder with datafiles."""
    assert os.path.exists("../data")


def test_src():
    """Passes if user's working directory contains src package directory."""
    assert os.path.exists("../src")


def test_license():
    """Passes if package directory contains LICENSE."""
    assert os.path.exists("../src/LICENSE")


def test_readme():
    """Passes if package directory contains documentation."""
    assert os.path.exists("../src/README.md")


def test_setup():
    """Passes if package directory contains setup.py file."""
    assert os.path.exists("../src/setup.py")


def test_data_examples():
    """Passes if package directory contains example datafiles to work on."""
    assert os.path.exists("../src/h2activity/data_examples")
