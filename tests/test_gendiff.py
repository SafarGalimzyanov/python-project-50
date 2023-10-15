import pytest
from gendiff.gendiff import generate_diff as g_d


def get_json_text(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        d = json.load(f)
    return d


@pytest.fixture(name='json_regular')
def _json_regular() -> str:
    return 'tests/fixtures/json_regular.json'

@pytest.fixture(name='json_same_values')
def _json_regular() -> str:
    return 'tests/fixtures/json_same_values.json'

@pytest.fixture(name='json_unique_values')
def _json_regular() -> str:
    return 'tests/fixtures/json_unique_values.json'
@pytest.fixture(name='json_unique_pairs')
def _json_unique_pairs() -> str:
    return 'tests/fixtures/json_unique_pairs.json'
@pytest.fixture(name='json_empty')
def _json_regular() -> str:
    return 'tests/fixtures/json_empty.json'


def test_generate_diff_json():
    reg_and_same_value =
    '{\n\n    1k: 1v\n    2k: 1v\n  - 3k: 3v\n  + 3k: 1v\n\n}'
    reg_and_unique =
    '{\n\n    1k: 1v\n  - 2K: 1v\n  + 2k: 2v\n    3k: 3v\n}'
    reg_and_empty =
    '{\n\n  - 1k: 1v\n  - 2k: 1v\n  - 3k: 3v\n\n}'
    same_values_and_unique_values =
    '{\n\n    1k: 1v\n  - 2k: 1v\n  + 2k: 2v\n  - 3k: 1v\n  + 3k: 3v\n}'
    same_values_and_empty =
    '{\n\n  - 1k: 1v\n  - 2k: 1v\n  - 3k: 1v\n}'
    unique_values_and_empty =
    '{\n\n  - 1k: 1v\n  - 2k: 2v\n  - 3k: 3v\n}'
    assert g_d('json_regular', 'json_empty') == reg_and_same_value



print(g_d(json_regular, json_regular))
