black:
	black src

flake8:
	flake8 src

pylint:
	pylint src

all: black flake8 pylint 
