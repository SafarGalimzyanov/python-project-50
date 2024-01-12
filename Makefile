install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

check:
	selfcheck test lint

build:
	check
	poetry build

b-i:
	python3 -m pip install --user dist/*.whl --force-reinstall ; poetry build ; poetry install ; gendiff f1.json f2.json ; gendiff f1.yml f2.yaml

s:
	vim gendiff/scripts/gendiff_script.py

l-g:
	poetry run flake8 gendiff

v-g:
	vim gendiff/gendiff.py

l-t:
	poetry run flake8 tests

v-t:
	vim tests/test_gendiff.py

r-t:
	poetry run python3 -m tests.test_gendiff

t:
	python3 -m pip install --user dist/*.whl --force-reinstall ; poetry build ; poetry install ;install:
	poetry install
