install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
b-i:
	poetry build ; poetry install ; python3 -m pip install --user dist/*.whl --force-reinstall ; gendiff F1.json F2.json ; gendiff F1.yaml F2.yaml 
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
