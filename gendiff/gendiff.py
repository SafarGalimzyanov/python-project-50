import json
import yaml
from gendiff.stylize import stylize
from gendiff.uniform import uniform


def load(file_path: str):
    file_format = file_path.split('.')[-1]
    with open(file_path, 'r') as f:
        if file_format in ('yaml', 'yml'):
            return yaml.safe_load(f)
        return json.load(f)


def generate_diff(file1_path: str, file2_path: str, style: str = ''):
    d1, d2 = load(file1_path), load(file2_path)
    if not d1 and not d2:
        return ''
    return stylize(uniform(d1, d2), style)
