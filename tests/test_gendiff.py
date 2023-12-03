import pytest
from gendiff.gendiff import generate_diff as g_d


def get_json_text(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        d = json.load(f)
    return d


DIFF = get_json_text('tests/test_permanent_diff')


@pytest.fixture(name='json_1')
def _json_regular() -> str:
    return 'tests/fixtures/file1.json'

@pytest.fixture(name='json_2')
def _json_regular() -> str:
    return 'tests/fixtures/file2.json'

@pytest.fixture(name='yaml_1')
def _json_regular() -> str:
    return 'tests/fixtures/file1.yml'

@pytest.fixture(name='yaml_2')
def _json_regular() -> str:
    return 'tests/fixtures/file2.yml'

def test_generate_diff():
    assert g_d('json_1', 'json_2') == DIFF
    assert g_d('yaml_1', 'yaml_2') == DIFF
