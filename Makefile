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
b:
	poetry build ; poetry install ; python3 -m pip install --user dist/*.whl --force-reinstall ; gendiff -f plain F1.json F2.json 
t:
	tree -I __*__***

g:	
	echo --------------- ; gendiff -f plain F1.json F2.json

te:
	pytest
