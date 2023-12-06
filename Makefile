install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest ...

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check:
	selfcheck test lint

build:
	check poetry build

p-i:
	pip install .

b-i:
	poetry build ; poetry install

l-g:
	poetry run flake8 gendiff

v-g:
	vim gendiff/gendiff.py

l-t:
	poetry run flake8 tests

v-t:
	vim tests/test_gendiff.py
r-tt:
	poetry run python3 -m tests.test_gendiff
