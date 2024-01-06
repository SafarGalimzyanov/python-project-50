import json, yaml
import pytest
from gendiff.gendiff_engine import generate_diff
from gendiff.gendiff_parse import generate_parse


def get_text(file_path: str):
    with open(file_path, 'r') as f:
        data = f.read()
    return data.strip()


DIFF = get_text('tests/fixtures/test_permanent_diff')
#json_1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
#json_2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

@pytest.fixture(name='json_1')
def j_1() -> str:
    return 'tests/fixtures/file1.json'

@pytest.fixture(name='json_2')
def j_2() -> str:
    return 'tests/fixtures/file2.json'

@pytest.fixture(name='yaml_1')
def y_1() -> str:
    return 'tests/fixtures/file1.yml'

@pytest.fixture(name='yaml_2')
def y_2() -> str:
    return 'tests/fixtures/file2.yml'

def test_generate_diff(json_1, json_2, yaml_1, yaml_2):
    assert generate_diff(*generate_parse(json_1, json_2)) == DIFF
    assert generate_diff(*generate_parse(yaml_1, yaml_2)) == DIFF
