black:
	black activity_package/h2activity/src

flake8:
	flake8 activity_package/h2activity/src

pylint:
	pylint activity_package/h2activity/src

all: black flake8 pylint 
