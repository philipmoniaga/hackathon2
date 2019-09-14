clean: 
	rm -rf src/*/*.pyc
	rm -rf src/*/__pycache__
tests:
	cd src/tests && pytest
lint:
	flake8 src/*/*.py --exclude=src/tests/*.py