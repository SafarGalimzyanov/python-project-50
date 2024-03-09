import json
from style.stylize import get_result


def get_json(d1, d2):
    return json.dumps({'file1': d1, 'file2': d2})


def compare(d1, d2, style: str, depth: int = 4, indent: str = 2*' ', ancestors: str = '') -> str:
    result = ''
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
    for key in keys:
        v1 = d1.get(key)
        v2 = d2.get(key)
        params = (key, v1, v2, style, depth, indent, ancestors + '.' + str(key))

        if key in d1 and key in d2:
            if v1 != v2:
                if type(v1) is dict and type(v2) is dict:
                    result += f'{indent}  {key}: {"{"}\n' if style != 'plain' else ''
                    result += compare(v1, v2, style, depth+4, indent+4*' ', ancestors + '.' + str(key))
                    result += f'{indent}  {"}"}\n' if style != 'plain' else ''
                else:
                    result += get_result(params, 'updated')
            else:
                result += get_result(params, 'same')
        elif key in d1 and key not in d2:
            result += get_result(params, 'removed')
        else:
            result += get_result(params, 'added')

    return result


def generate_diff(d1: dict = {}, d2: dict = {}, style: str = ''):
    match style:
        case 'plain':
            return compare(d1, d2, 'plain')[:-1]
        case 'json':
            return get_json(d1, d2)
        case _:
            return '{\n' + compare(d1, d2, '') + '}'
