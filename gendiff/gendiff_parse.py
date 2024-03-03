import json, yaml
from typing import TextIO


def generate_parse(file1_path: str, file2_path: str, style: str='') -> str:
    file_format = file1_path.split('.')[-1] #get text after dot (file.???)-> json or yaml/yml

    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        if file_format in ('yaml', 'yml'):
            return yaml.safe_load(f1), yaml.safe_load(f2), style #doesn't work with yaml.load
        return json.load(f1), json.load(f2), style
