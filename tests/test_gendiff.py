from gendiff import generate_diff


def get_text(file_path: str):
    with open(file_path, 'r') as f:
        data = f.read()
    return data.strip()


DIFF_DEFAULT_FORMAT = get_text('tests/fixtures/test_default_format')
DIFF_PLAIN_FORMAT = get_text('tests/fixtures/test_plain_format')
DIFF_JSON_FORMAT = get_text('tests/fixtures/test_json_format.json')
JSON_1 = 'tests/fixtures/json/file1.json'
JSON_2 = 'tests/fixtures/json/file2.json'
JSON_3 = 'tests/fixtures/json/file3.json'
JSON_4 = 'tests/fixtures/json/file4.json'
JSON_5 = 'tests/fixtures/json/file5.json'
JSON_6 = 'tests/fixtures/json/file6.json'
JSON_7 = 'tests/fixtures/json/file7.json'
JSON_8 = 'tests/fixtures/json/file8.json'
JSON_9 = 'tests/fixtures/json/file9.json'
JSON_10 = 'tests/fixtures/json/file10.json'
JSON_11 = 'tests/fixtures/json/file11.json'
JSON_12 = 'tests/fixtures/json/file12.json'

YAML_1 = 'tests/fixtures/yaml/file1.yaml'
YAML_2 = 'tests/fixtures/yaml/file2.yaml'
YAML_3 = 'tests/fixtures/yaml/file3.yml'
YAML_4 = 'tests/fixtures/yaml/file4.yaml'
YAML_5 = 'tests/fixtures/yaml/file5.yml'
YAML_6 = 'tests/fixtures/yaml/file6.yaml'
YAML_7 = 'tests/fixtures/yaml/file7.yml'
YAML_8 = 'tests/fixtures/yaml/file8.yaml'
YAML_9 = 'tests/fixtures/yaml/file9.yml'
YAML_10 = 'tests/fixtures/yaml/file10.yaml'
YAML_11 = 'tests/fixtures/yaml/file11.yml'
YAML_12 = 'tests/fixtures/yaml/file12.yml'


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
