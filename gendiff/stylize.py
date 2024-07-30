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
    previous_key_order = []
    '''
    {[k1, k2, k2.5], value0, same}
    {[k1, k2, k3, k4], value, same}
    k1:
        k2:
    '''

    for d in uniformed_dicts:
        result += style_functions.get(style)(d, previous_key_order)
        previous_key_order = d.get('key_order')

    return result
