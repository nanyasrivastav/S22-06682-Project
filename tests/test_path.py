import os 
def test_data():
    assert os.path.exists('./data')

def test_license():
    assert os.path.exists('./h2activity_package/LICENSE.md')

def test_readme():
    assert os.path.exists('./h2activity_package/README.md')

def test_src():
    assert os.path.exists('./h2activity_package/h2activity/src')

def test_data_examples():
    assert os.path.exists('./h2activity_package/h2activity/data_examples')