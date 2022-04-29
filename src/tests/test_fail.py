"""Tests that pass if the function fails to return value."""
import pytest  
from utilities import display_head, max_h2, stats


def test_fail_displayhead():
    """TypeError raised if function is called with file arguments."""
    with pytest.raises(TypeError):
        display_head()  # pylint: disable=no-value-for-parameter


def test_fail_maxh2():
    """TypeError raised if function is called with no file and option arguments."""
    with pytest.raises(TypeError):
        max_h2()  # pylint: disable=no-value-for-parameter


def test_fail_stats():
    """TypeError raised if function is called with no file arguments."""
    with pytest.raises(TypeError):
        stats()  # pylint: disable=no-value-for-parameter
