'''
def get_dict(key, v1: dict, v2: dict, style: str, indent: str, ancestors: str) -> str:
    if style != 'plain':
        start = f'{indent}  {key}: {"{"}\n'
        end = f'{indent}  {"}"}\n'
    return compare(v1, v2, style, indent + 4 * ' ', ancestors + '.' + str(key))

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

def uniform(d1: dict={}, d2: dict={}) -> list:
    result = list()

    def append_to_result(key, change: str, value, updated_value = None) -> dict:
        if updated_value:
            return {'key': key, 'change': change, 'value': value, 'updated_value': updated_value}
        return {'key': key, 'change': change, 'value': value}

    def compare(d1: dict = {}, d2: dict = {}, key_order: list = []) -> None:
        keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
        for key in keys:
            value_1 = d1.get(key)
            value_2 = d2.get(key)
            key_order.append(key)

            if key in d1 and key in d2:
                if value_1 != value_2:
                    if type(value_1) is dict and type(value_2) is dict:
                        compare(value_1, value_2, key_order)
                    else:
                        result.append(append_(key_order, 'updated', value_1, value_2))
                else:
                    result.append(append_(key_order, 'same', value_1))
            elif key in d1 and key not in d2:
                result.append(append_(key_order, 'removed', value_1))
            else:
                result.append(append_(key_order, 'added', value_2))

    compare(d1, d2)
    return result
