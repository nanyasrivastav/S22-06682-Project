import os 
def test_data():
    assert os.path.exists('../data')

def test_license():
    assert os.path.exists('LICENSE.md')

def test_readme():
    assert os.path.exists('README.md')

def test_src():
    assert os.path.exists('h2activity/src')