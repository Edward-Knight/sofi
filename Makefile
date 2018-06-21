export WORKON_HOME=.venvs
export ENV_LOCATION ?= $(shell pipenv --venv)
export WD:=$(CURDIR)

.PHONY: setup install dist test run_sample  system_test clean

setup:
	@pipenv install --skip-lock
	@pipenv install --skip-lock --dev

install:
	@pipenv run pip install  .

build:
	@rm -rf dist/
	@rm -rf build/
	@pipenv run python setup.py sdist

test:
	@pipenv run pytest test

system_test:
	$(eval timestamp=$(shell date "+%Y-%m-%dT%H:%M:%S"))
	@pipenv run pytest system_test/test.py --driver Chrome --headless -s \
	--html=test_reports/${timestamp}.html

run_sample:
	@pipenv run python sample_test/sample.py


clean:
	@rm -rf ${WORKON_HOME}
	@rm -rf dist/
	@rm -rf build/
	@rm -rf test_reports/
	@rm -rf sofi.egg-info/
	@rm -rf .pytest_cache/