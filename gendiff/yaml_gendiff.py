import json
from typing import TextIO


def generate_diff(file1_path: str, file2_path: str) -> str:
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)
        d_in1_in2, d_in1 = dict(), dict()
        for key in d1:
            d = {key: d1.get(key)}
            if d1.get(key) == d2.get(key):
                d_in1_in2.update(d)
                d2.pop(key)
            else:
                d_in1.update(d)

        keys = sorted(list(d_in1_in2.keys()) + list(d_in1.keys()) + list(d2.keys()))
        start = '{\n\n'
        end = '\n}'
        result = ''
        for key in keys:
            if key in d_in1:
                result += f'  - {key}: {d_in1.get(key)}\n'
            elif key in d2:
                result += f'  + {key}: {d2.get(key)}\n'
            else:
                result += f'    {key}: {d_in1_in2.get(key)}\n'
            
        return start + result + end
