import json
import yaml
from gendiff import generate_diff
from gendiff.uniform import uniform


def load(file_path1: str, file_path2: str):
    file_format = file_path1.split('.')[-1]
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        if file_format in ('yaml', 'yml'):
            return yaml.safe_load(f1), yaml.safe_load(f2)
        return json.load(f1), json.load(f2)


def get_text(file_path: str):
    with open(file_path, 'r') as f:
        data = f.read()
    return data.strip()


UNIFORM_1_2 = get_text('tests/fixtures/test_uniform_1_2')


DIFF_DEFAULT_FORMAT_1_2 = get_text('tests/fixtures/test_default_format_1_2')
DIFF_DEFAULT_FORMAT_2_1 = get_text('tests/fixtures/test_default_format_2_1')
DIFF_DEFAULT_FORMAT_3_4 = get_text('tests/fixtures/test_default_format_3_4')
DIFF_DEFAULT_FORMAT_4_3 = get_text('tests/fixtures/test_default_format_4_3')
DIFF_DEFAULT_FORMAT_5_6 = get_text('tests/fixtures/test_default_format_5_6')
DIFF_DEFAULT_FORMAT_6_5 = get_text('tests/fixtures/test_default_format_6_5')
DIFF_DEFAULT_FORMAT_7_8 = get_text('tests/fixtures/test_default_format_7_8')
DIFF_DEFAULT_FORMAT_8_7 = get_text('tests/fixtures/test_default_format_8_7')
DIFF_DEFAULT_FORMAT_9_10 = get_text('tests/fixtures/test_default_format_9_10')
DIFF_DEFAULT_FORMAT_10_9 = get_text('tests/fixtures/test_default_format__10_9')
DIFF_DEFAULT_FORMAT_11_12 = get_text('tests/fixtures/test_default_format__11_12')
DIFF_DEFAULT_FORMAT_12_11 = get_text('tests/fixtures/test_default_format__12_11')

DIFF_PLAIN_FORMAT_1_2 = get_text('tests/fixtures/test_plain_format_1_2')
DIFF_PLAIN_FORMAT_2_1 = get_text('tests/fixtures/test_plain_format_2_1')
DIFF_PLAIN_FORMAT_3_4 = get_text('tests/fixtures/test_plain_format_3_4')
DIFF_PLAIN_FORMAT_4_3 = get_text('tests/fixtures/test_plain_format_4_3')
DIFF_PLAIN_FORMAT_5_6 = get_text('tests/fixtures/test_plain_format_5_6')
DIFF_PLAIN_FORMAT_6_5 = get_text('tests/fixtures/test_plain_format_6_5')
DIFF_PLAIN_FORMAT_7_8 = get_text('tests/fixtures/test_plain_format_7_8')
DIFF_PLAIN_FORMAT_8_7 = get_text('tests/fixtures/test_plain_format_8_7')
DIFF_PLAIN_FORMAT_9_10 = get_text('tests/fixtures/test_plain_format_9_10')
DIFF_PLAIN_FORMAT_10_9 = get_text('tests/fixtures/test_plain_format__10_9')
DIFF_PLAIN_FORMAT_11_12 = get_text('tests/fixtures/test_plain_format__11_12')
DIFF_PLAIN_FORMAT_12_11 = get_text('tests/fixtures/test_plain_format__12_11')

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
JSON_10 = 'tests/fixtures/json/file_10.json'
JSON_11 = 'tests/fixtures/json/file_11.json'
JSON_12 = 'tests/fixtures/json/file_12.json'

YAML_1 = 'tests/fixtures/yaml/file1.yaml'
YAML_2 = 'tests/fixtures/yaml/file2.yml'
YAML_3 = 'tests/fixtures/yaml/file3.yaml'
YAML_4 = 'tests/fixtures/yaml/file4.yml'
YAML_5 = 'tests/fixtures/yaml/file5.yaml'
YAML_6 = 'tests/fixtures/yaml/file6.yml'
YAML_7 = 'tests/fixtures/yaml/file7.yaml'
YAML_8 = 'tests/fixtures/yaml/file8.yml'
YAML_9 = 'tests/fixtures/yaml/file9.yaml'
YAML_10 = 'tests/fixtures/yaml/file_10.yml'
YAML_11 = 'tests/fixtures/yaml/file_11.yaml'
YAML_12 = 'tests/fixtures/yaml/file_12.yml'


def test_gendiff_json_regular_style():
    assert generate_diff(JSON_1, JSON_2) == DIFF_DEFAULT_FORMAT_1_2
    assert generate_diff(JSON_2, JSON_1) == DIFF_DEFAULT_FORMAT_2_1
    assert generate_diff(JSON_3, JSON_4) == DIFF_DEFAULT_FORMAT_3_4
    assert generate_diff(JSON_4, JSON_3) == DIFF_DEFAULT_FORMAT_4_3
    assert generate_diff(JSON_5, JSON_6) == DIFF_DEFAULT_FORMAT_5_6
    assert generate_diff(JSON_6, JSON_5) == DIFF_DEFAULT_FORMAT_6_5
    assert generate_diff(JSON_7, JSON_8) == DIFF_DEFAULT_FORMAT_7_8
    assert generate_diff(JSON_8, JSON_7) == DIFF_DEFAULT_FORMAT_8_7
    assert generate_diff(JSON_9, JSON_10) == DIFF_DEFAULT_FORMAT_9_10
    assert generate_diff(JSON_10, JSON_9) == DIFF_DEFAULT_FORMAT_10_9
    assert generate_diff(JSON_11, JSON_12) == DIFF_DEFAULT_FORMAT_11_12
    assert generate_diff(JSON_12, JSON_11) == DIFF_DEFAULT_FORMAT_12_11


def test_gendiff_yaml_regular_style():
    assert generate_diff(YAML_1, YAML_2) == DIFF_DEFAULT_FORMAT_1_2
    assert generate_diff(YAML_2, YAML_1) == DIFF_DEFAULT_FORMAT_2_1
    assert generate_diff(YAML_3, YAML_4) == DIFF_DEFAULT_FORMAT_3_4
    assert generate_diff(YAML_4, YAML_3) == DIFF_DEFAULT_FORMAT_4_3
    assert generate_diff(YAML_5, YAML_6) == DIFF_DEFAULT_FORMAT_5_6
    assert generate_diff(YAML_6, YAML_5) == DIFF_DEFAULT_FORMAT_6_5
    assert generate_diff(YAML_7, YAML_8) == DIFF_DEFAULT_FORMAT_7_8
    assert generate_diff(YAML_8, YAML_7) == DIFF_DEFAULT_FORMAT_8_7
    assert generate_diff(YAML_9, YAML_10) == DIFF_DEFAULT_FORMAT_9_10
    assert generate_diff(YAML_10, YAML_9) == DIFF_DEFAULT_FORMAT_10_9
    assert generate_diff(YAML_11, YAML_12) == DIFF_DEFAULT_FORMAT_11_12
    assert generate_diff(YAML_12, YAML_11) == DIFF_DEFAULT_FORMAT_12_11


def test_gendiff_json_plain_style():
    assert generate_diff(JSON_1, JSON_2, 'plain') == DIFF_PLAIN_FORMAT_1_2
    assert generate_diff(JSON_2, JSON_1, 'plain') == DIFF_PLAIN_FORMAT_2_1
    assert generate_diff(JSON_3, JSON_4, 'plain') == DIFF_PLAIN_FORMAT_3_4
    assert generate_diff(JSON_4, JSON_3, 'plain') == DIFF_PLAIN_FORMAT_4_3
    assert generate_diff(JSON_5, JSON_6, 'plain') == DIFF_PLAIN_FORMAT_5_6
    assert generate_diff(JSON_6, JSON_5, 'plain') == DIFF_PLAIN_FORMAT_6_5
    assert generate_diff(JSON_7, JSON_8, 'plain') == DIFF_PLAIN_FORMAT_7_8
    assert generate_diff(JSON_8, JSON_7, 'plain') == DIFF_PLAIN_FORMAT_8_7
    assert generate_diff(JSON_9, JSON_10, 'plain') == DIFF_PLAIN_FORMAT_9_10
    assert generate_diff(JSON_10, JSON_9, 'plain') == DIFF_PLAIN_FORMAT_10_9
    assert generate_diff(JSON_11, JSON_12, 'plain') == DIFF_PLAIN_FORMAT_11_12
    assert generate_diff(JSON_12, JSON_11, 'plain') == DIFF_PLAIN_FORMAT_12_11


def test_gendiff_yaml_plain_style():
    assert generate_diff(YAML_1, YAML_2, 'plain') == DIFF_PLAIN_FORMAT_1_2
    assert generate_diff(YAML_2, YAML_1, 'plain') == DIFF_PLAIN_FORMAT_2_1
    assert generate_diff(YAML_3, YAML_4, 'plain') == DIFF_PLAIN_FORMAT_3_4
    assert generate_diff(YAML_4, YAML_3, 'plain') == DIFF_PLAIN_FORMAT_4_3
    assert generate_diff(YAML_5, YAML_6, 'plain') == DIFF_PLAIN_FORMAT_5_6
    assert generate_diff(YAML_6, YAML_5, 'plain') == DIFF_PLAIN_FORMAT_6_5
    assert generate_diff(YAML_7, YAML_8, 'plain') == DIFF_PLAIN_FORMAT_7_8
    assert generate_diff(YAML_8, YAML_7, 'plain') == DIFF_PLAIN_FORMAT_8_7
    assert generate_diff(YAML_9, YAML_10, 'plain') == DIFF_PLAIN_FORMAT_9_10
    assert generate_diff(YAML_10, YAML_9, 'plain') == DIFF_PLAIN_FORMAT_10_9
    assert generate_diff(YAML_11, YAML_12, 'plain') == DIFF_PLAIN_FORMAT_11_12
    assert generate_diff(YAML_12, YAML_11, 'plain') == DIFF_PLAIN_FORMAT_12_11


def test_gendiff_json_json_style():
    assert generate_diff(JSON_9, JSON_10, 'json') == DIFF_JSON_FORMAT


def test_uniform():
    assert uniform(*load(JSON_1, JSON_2)) == []
