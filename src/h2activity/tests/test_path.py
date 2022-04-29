"""Tests that pass iff project contains necessary files."""
import os


def test_data():
    """Passes if working directory has a data folder with datafiles."""
    assert os.path.exists("../../data")


def test_src():
    """Passes if working directory contains src package."""
    assert os.path.exists("../../src")


def test_license():
    """Passes if package contains LICENSE."""
    assert os.path.exists("../../src/LICENSE")


def test_readme():
    """Passes if package contains README/ documentation."""
    assert os.path.exists("../../src/README.md")


def test_setup():
    """Passes if package contains setup.py."""
    assert os.path.exists("../../src/setup.py")


def test_data_examples():
    """Passes if package contains example datafiles to work on."""
    assert os.path.exists("../../src/h2activity/data_examples")
