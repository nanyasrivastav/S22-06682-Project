black:
	black src

flake8:
	flake8 --max-line-length 85 src

pylint:
	pylint src

all: black flake8 pylint 
