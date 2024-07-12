from styles.style_plain import plain
from styles.style_regular import regular
from styles.style_json import json_


def stylize(uniformed_dicts: list = [], style: str = 'regular') -> str:
    style_functions = {
            'plain': plain,
            'regular': regular,
            'json': json_,
            }
    if style is None:
        style = 'regular'
    result = ''
    for d in uniformed_dicts:
        result += style_functions.get(style)(d)

    return result
