from styles.plain import plain
from styles.regular import regular
from styles.json import json_


def stylize(uniformed_dicts: list=[], style: str) -> str:
    style_functions = {
            'plain': plain,
            'regular': regular,
            'json': json_
            }
    result = ''
    for d in uniformed_dicts:
        result += style_functions.get(style)(d)

    return result
