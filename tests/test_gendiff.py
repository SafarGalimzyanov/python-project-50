import json, yaml
import pytest
from gendiff.gendiff import generate_diff
from gendiff.gendiff_parse import generate_parse


def get_text(file_path: str):
    with open(file_path, 'r') as f:
        data = f.read()
    return data.strip()


DIFF_DEFAULT_FORMAT = get_text('tests/fixtures/test_default_format')
DIFF_PLAIN_FORMAT = get_text('tests/fixtures/test_plain_format')
DIFF_JSON_FORMAT = get_text('tests/fixtures/test_json_format.json')
JSON_1 = 'tests/fixtures/json/file1.json'
JSON_2 = 'tests/fixtures/json/file2.json'
YAML_1 = 'tests/fixtures/yaml/file1.yml'
YAML_2 = 'tests/fixtures/yaml/file2.yaml'

def test_gendiff_json_default_style():
    assert generate_diff(JSON_1, JSON_2) == DIFF_DEFAULT_FORMAT

def test_gendiff_yaml_default_style():
    assert generate_diff(YAML_1, YAML_2) == DIFF_DEFAULT_FORMAT

def test_gendiff_json_plain_style():
    assert generate_diff(JSON_1, JSON_2, 'plain') == DIFF_PLAIN_FORMAT

def test_gendiff_yaml_plain_style():
    assert generate_diff(YAML_1, YAML_2, 'plain') == DIFF_PLAIN_FORMAT

def test_gendiff_json_json_style():
    assert generate_diff(JSON_1, JSON_2, 'json') == DIFF_JSON_FORMAT
