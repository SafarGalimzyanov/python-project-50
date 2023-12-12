import json, yaml
from typing import TextIO


def generate_parse(file1_path: str, file2_path: str) -> str:
    file_format = file1_path.split('.')[-1]
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        if file_format == 'json':
            print('\n\nJSON\n\n')
            return json.load(f1), json.load(f2)
        return yaml.load(f1), yaml.load(f2)
