"""Setup file to indicate package is pip installable. """
from setuptools import setup

setup(
    name="h2activity",
    version="1.0",
    description="Display and report summary of dataset(s)",
    maintainer="Ananya Srivastava",
    maintainer_email="ananyasr@andrew.cmu.edu",
    license="GPL",
    packages=["h2activity"],
    scripts=[
        "h2activity/start.py",
        "h2activity/display.py",
        "h2activity/high_activity.py",
        "h2activity/stats.py",
    ],
    include_package_data=True,
    long_description="""\
Summary of High Throughput Experiment Dataset(s)
==============
Command line utilities to read and display dataset(s) and
output its summarized results.""",
)
