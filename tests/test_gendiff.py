import pytest
from gendiff.gendiff import generate_diff as g_d


def get_json_text(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        d = json.load(f)
    return d


@pytest.fixture(name='json_regular')
def _json_regular() -> str:
    return 'tests/fixtures/json_regular.json'

@pytest.fixture(name='json_same_val')
def _json_regular() -> str:
    return 'tests/fixtures/json_same_val.json'

@pytest.fixture(name='json_unique_val')
def _json_regular() -> str:
    return 'tests/fixtures/json_unique_val.json'

@pytest.fixture(name='json_unique_pair')
def _json_unique_pairs() -> str:
    return 'tests/fixtures/json_unique_pair.json'

@pytest.fixture(name='json_empty')
def _json_regular() -> str:
    return 'tests/fixtures/json_empty.json'


def test_generate_diff_json():
    reg_and_same_val =
    '{\n\n    1k: 1v\n    2k: 1v\n  - 3k: 3v\n  + 3k: 1v\n\n}'
    reg_and_unique_val =
    '{\n\n    1k: 1v\n  - 2K: 1v\n  + 2k: 2v\n    3k: 3v\n\n}'
    reg_and_unique_pair =
    '{\n\n  + 0k: 0v\n  - 1k: 1v\n  - 2k: 1v\n  + 4k: 1v\n  - 3k: 3v\n  + true: []\n\n}'
    reg_and_empty =
    '{\n\n  - 1k: 1v\n  - 2k: 1v\n  - 3k: 3v\n\n}'
    same_val_and_unique_val =
    '{\n\n    1k: 1v\n  - 2k: 1v\n  + 2k: 2v\n  - 3k: 1v\n  + 3k: 3v\n\n}'
    same_val_and_empty =
    '{\n\n  - 1k: 1v\n  - 2k: 1v\n  - 3k: 1v\n\n}'
    unique_val_and_empty =
    '{\n\n  - 1k: 1v\n  - 2k: 2v\n  - 3k: 3v\n\n}'

    assert g_d('json_regular', 'json_same_val') == reg_and_same_val
    assert g_d('json_regular', 'json_unique_val') == reg_and_unique_val
    assert g_d('json_regular', 'json_unique') == reg_and_unique_pair
    assert g_d('json_regular', 'json_empty') == reg_and_empty
    assert g_d('json_same_val', 'json_unique_val') == same_val_and_unique_val
    assert g_d('json_same_val', 'json_empty') == same_val_and_empty
    assert g_d('json_unique_val', 'json_empty') == unique_val_and_empty



print(g_d(json_regular, json_regular))
