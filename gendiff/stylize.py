from styles.style_plain import plain
from styles.style_regular import regular
from styles.style_json import json_


_NOT_PROVIDED = object()


def stylize(uniformed_dicts: list = _NOT_PROVIDED, style: str = '') -> str:
    if uniformed_dicts is _NOT_PROVIDED:
        uniformed_dicts = []

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

    match style:
        case 'regular':
            return '{\n' + result + '}'
        case 'plain':
            return result[:-1]
        case _:
            return result
