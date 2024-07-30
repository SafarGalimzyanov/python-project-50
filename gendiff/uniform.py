from copy import deepcopy

'''
def uniform(d1: dict = {}, d2: dict = {}) -> list:
    result = []
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
                        result.append(uniformed((key_order, 'updated', value_1, value_2)))
                else:
                    result.append(uniformed((key_order, 'same', value_1)))
            elif key in d1 and key not in d2:
                result.append(uniformed((key_order, 'removed', value_1)))
            else:
                result.append(uniformed((key_order, 'added', value_2)))


    def uniformed(key_order: list = [], change: str = 'DEFAULT_CHANGE', value = None, updated_value = None) -> dict:
        return {'key_order': key_order, 'change': change, 'value': value, 'updated_value': updated_value}

    compare(d1, d2)
    return result
'''

def get_indent(key_order: list, value, depth: int) -> dict:
    result = {
            'len_indent': len_indent,
            'dict_indent': dict_indent,
    }
    len_indent = len(key_order)
    
    def get_dict_indent():
        #case 0: none before
        #case 1: there is a change before in the same depth
        #case 2: opening a dict
        #case 3: after a closed dict

        return dict_indent

    dict_indent = get_dict_indent()

    return {'len_inden': len_indent, 'dict_indent': dict_indent}


def compare(d1: dict = {}, d2: dict = {}, key_order: list = [], depth: int=0) -> None:
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
    key_order.append(keys[0])
    depth += 1
    for key in keys:
        value_1 = d1.get(key)
        value_2 = d2.get(key)
        key_order[-1] = key
        indent = get_indent(key_order, value, depth)

        if key in d1 and key in d2:
            if value_1 != value_2:
                if type(value_1) is dict and type(value_2) is dict:
                    yield from compare(value_1, value_2, deepcopy(key_order), depth)
                else:
                    yield ('updated', deepcopy(key_order), value_1, value_2, indent)
            else:
                yield ('same', deepcopy(key_order), value_1, indent)
        elif key in d1 and key not in d2:
            yield ('removed', deepcopy(key_order), value_1, indent)
        else:
            yield ('added',  deepcopy(key_order), value_2, indent)


def uniformed(t) -> dict:
    change, key_order, value, *updated_value = t
    if updated_value:
        return {'change': change, 'key_order': key_order, 'value': value, 'updated_value': updated_value[0]}
    return {'change': change, 'key_order': key_order, 'value': value}


def uniform(d1: dict = {}, d2: dict = {}) -> list:
    return [uniformed(result) for result in list(compare(d1, d2))]
