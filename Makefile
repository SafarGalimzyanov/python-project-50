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

bi:
	poetry build ; poetry install

l-g:
	poetry run flake8 gendiff

v-g:
	vim gendiff/gendiff.py

l-t:
	poetry run flake8 tests

v-t:
	vim tests/test_gendiff.py

r:
	poetry run gendiff

t:
	poetry run python3 -m tests.test_gendiff
