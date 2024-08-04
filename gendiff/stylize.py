from styles.style_plain import plain
from styles.style_regular import regular
from styles.style_json import json_


def stylize(uniformed_dicts: list = [], style: str = 'regular') -> str:
    style_functions = {
            'plain': plain,
            'regular': regular,
            'json': json_,
            }
    if style not in style_functions:
        style = 'regular'

    result = ''
    previous_key_order = []
    for d in uniformed_dicts:
        result += style_functions.get(style)(d, previous_key_order)
        previous_key_order = d.get('key_order')

    if style == 'regular':
        return '{\n' + result + '}'
    return result
