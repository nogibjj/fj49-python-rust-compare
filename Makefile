install:
	pip install --upgrade pip &&\
		pip install -r python/requirements.txt

test_python:
	python -m pytest -vv --cov=python

# format_python:	
# 	black python/*.py 

lint_python: #lol
	pylint --disable=R,C 

build_rust:
	cd rust && cargo build

run_rust:
	cd rust && cargo run

test_rust:
	@echo "Testing all projects with cargo"
	./test.sh

build_and_run: build_rust run_rust

test: #no testing

all: install refactor_python build_and_run test
