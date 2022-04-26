from setuptools import setup

setup(name='h2activity',
      version='0.0.1',
      description='Summary of dataset(s)',
      maintainer='Ananya Srivastava',
      maintainer_email='ananyasr@andrew.cmu.edu',
      license='GPL',
      packages=['h2activity'],
      scripts=['h2activity/src/display.py', 'h2activity/src/display_all.py', 'h2activity/src/display_one.py', 'h2activity/src/high_activity.py', 'h2activity/src/utilities.py'],
      long_description='''\
Summary of High Throughput Experiment Dataset(s) 
==============
Command line utilities to read datasets and
output its contents and summarized results.''')