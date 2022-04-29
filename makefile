black:
	black h2activity_package/h2activity/src

flake8:
	flake8 --max-line-length 83 h2activity_package/h2activity/src

pylint:
	pylint h2activity_package/h2activity/src

all: black flake8 pylint 
