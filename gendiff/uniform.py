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

def compare(d1: dict = {}, d2: dict = {}, key_order: list = []) -> None:
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
    key_order.append(keys[0])
    for key in keys:
        value_1 = d1.get(key)
        value_2 = d2.get(key)
        key_order[-1] = key

        if key in d1 and key in d2:
            if value_1 != value_2:
                if type(value_1) is dict and type(value_2) is dict:
                    yield from compare(value_1, value_2, deepcopy(key_order))
                else:
                    yield ('updated', deepcopy(key_order), value_1, value_2)
            else:
                yield ('same', deepcopy(key_order), value_1)
        elif key in d1 and key not in d2:
            yield ('removed', deepcopy(key_order), value_1)
        else:
            yield ('added',  deepcopy(key_order), value_2)


def uniformed(t) -> dict:
    change, key_order, value, *updated_value = t
    if updated_value:
        return {'change': change, 'key_order': key_order, 'value': value, 'updated_value': updated_value[0]}
    return {'change': change, 'key_order': key_order, 'value': value}


def uniform(d1: dict = {}, d2: dict = {}) -> list:
    return [uniformed(result) for result in list(compare(d1, d2))]
