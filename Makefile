# Build, package, test, and clean
PROJECT=testipynb
TESTDIR=tmp-test-dir
PYTEST_ARGS=../tests --cov-config=../.coveragerc --cov-report=term-missing --cov=$(PROJECT) -v
LINT_FILES=setup.py $(PROJECT)
BLACK_FILES=setup.py $(PROJECT)
FLAKE8_FILES=setup.py $(PROJECT)

help:
	@echo "Commands:"
	@echo ""
	@echo "  install   install in editable mode"
	@echo "  test      run the test suite (including doctests) and report coverage"
	@echo "  format    run black to automatically format the code"
	@echo "  check     run code style and quality checks (black and flake8)"
	@echo "  lint      run pylint for a deeper (and slower) quality check"
	@echo "  clean     clean up build and generated files"
	@echo "  docs      build the docs"
	@echo "  deploy    deploy to pypi"
	@echo ""

install:
	pip install --no-deps -e .

test:
	# Run a tmp folder to make sure the tests are run on the installed version
	mkdir -p $(TESTDIR)
	cd $(TESTDIR); MPLBACKEND='agg' pytest $(PYTEST_ARGS)
	cp $(TESTDIR)/.coverage* .
	rm -rvf $(TESTDIR)
	cd ..

format:
	black $(BLACK_FILES)

check:
	black --check $(BLACK_FILES)
	flake8 $(FLAKE8_FILES)

lint:
	pylint --jobs=0 $(LINT_FILES)


graphs:
	pyreverse -my -A -o pdf -p testipynb testipynb/**.py testipynb/**/**.py

docs:
	cd docs
	make html
	cd ..

deploy:
	python setup.py sdist bdist_wheel upload

clean:
	find . -name "*.pyc" -exec rm -v {} \;
	find . -name ".coverage.*" -exec rm -v {} \;
	rm -rvf build dist *.egg-info __pycache__ .coverage .cache .pytest_cache
