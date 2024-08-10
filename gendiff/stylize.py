from styles.style_plain import plain
from styles.style_regular import regular
from styles.style_json import json_


_NOT_PROVIDED = object()


def edit_regular(result: str) -> str:
    last_newline_index = result.rfind('\n')
    second_last_newline_index = result.rfind('\n', 0, last_newline_index)
    last_str = result[second_last_newline_index + 1:last_newline_index]

    possible_starts = ('    ', '  - ', '  + ')
    index = 0
    while last_str[index:4 + index] in possible_starts:
        index += 4
    for i in range(index - 4, 0, -4):
        result += f'{" " * i}}}\n'

    return '{\n' + result + '}'


def stylize(uniformed_dicts: list = _NOT_PROVIDED, style: str = '') -> str:
    if uniformed_dicts is _NOT_PROVIDED:
        uniformed_dicts = []

    style_functions = {'plain': plain, 'regular': regular, 'json': json_}
    if style not in style_functions:
        style = 'regular'

    result = ''
    previous_key_order = []
    for d in uniformed_dicts:
        result += style_functions.get(style)(d, previous_key_order)
        previous_key_order = d.get('key_order')

    match style:
        case 'regular':
            return edit_regular(result)
        case 'plain':
            return result[:-1]
        case _:
            return result
