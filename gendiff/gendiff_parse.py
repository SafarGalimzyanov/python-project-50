import json, yaml
from typing import TextIO


def generate_parse(file1_path: str, file2_path: str, print_format: str='') -> str:
    file_format = file1_path.split('.')[-1] #get str after dot -> json or yaml/yml
    
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        if file_format in ('yaml', 'yml'):
            return yaml.safe_load(f1), yaml.safe_load(f2), print_format
        return json.load(f1), json.load(f2), print_format
