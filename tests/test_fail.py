import pytest
#from h2activity_package.h2activity.src.utilities import display_head, max_h2, stats

def test_fail_displayhead():
    with pytest.raises(TypeError):
        h2activity_package.h2activity.src.utilities.display_head()

def test_fail_maxh2():
    with pytest.raises(TypeError):
        h2activity_package.h2activity.src.utilities.max_h2()

def test_fail_stats():
    with pytest.raises(TypeError):
        h2activity_package.h2activity.src.utilities.stats()