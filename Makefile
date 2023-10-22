install:
	pip install --upgrade pip &&\
		pip install -r python/requirements.txt

test_python:
	python -m pytest -vv --cov=python

format_python:	
	black python/*.py 

lint_python:
	pylint --disable=R,C --ignore-patterns=test_.*?py python/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor_python: format_python lint_python

build_rust:
	cd rust && cargo build

run_rust:
	cd rust && cargo run

test_rust:
	cd rust && cargo test

build_and_run: build_rust run_rust

test: #no testing

all: install refactor_python build_and_run test
