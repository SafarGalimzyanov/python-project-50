import json
import yaml
from uniform import uniform
from stylize import stylize




'''
def get_dict(key, v1: dict, v2: dict, style: str, indent: str, ancestors: str) -> str:
    start, end = '', ''
    if style != 'plain':
        start = f'{indent}  {key}: {"{"}\n'
        end = f'{indent}  {"}"}\n'
    return start + compare(v1, v2, style, indent + 4 * ' ', ancestors + '.' + str(key)) + end


def compare(d1: dict, d2: dict, style: str, indent: str = 2 * ' ', ancestors: str = '') -> str:
    result = ''
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
    for key in keys:
        v1 = d1.get(key)
        v2 = d2.get(key)
        params = (key, v1, v2, style, indent, ancestors + '.' + str(key))

        if key in d1 and key in d2:
            if v1 != v2:
                if type(v1) is dict and type(v2) is dict:
                    result += get_dict(key, v1, v2, style, indent, ancestors)
                else:
                    result += stylize(params, 'updated')
            else:
                result += stylize(params, 'same')
        elif key in d1 and key not in d2:
            result += stylize(params, 'removed')
        else:
            result += stylize(params, 'added')
    return result
'''

def generate_diff(file1_path: str, file2_path: str, style: str = ''):
    def load(file1_path: str, file2_path: str) -> str:
        file_format = file1_path.split('.')[-1]
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            if file_format in ('yaml', 'yml'):
                return yaml.safe_load(f1), yaml.safe_load(f2)
            return json.load(f1), json.load(f2)

    d1, d2 = load(file1_path, file2_path)
    return stylize(uniform(d1, d2), style)

'''
#уходит в stylize там 3 функции plain json other
    match style:
        case 'plain':
            return compare(d1, d2, 'plain')[:-1]
        case 'json':
            return get_json(d1, d2)
        case _:
            return '{\n' + compare(d1, d2, '') + '}'
    '''
