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
    for key in keys:
        value_1 = d1.get(key)
        value_2 = d2.get(key)
        key_order.append(key)

        if key in d1 and key in d2:
            if value_1 != value_2:
                if type(value_1) is dict and type(value_2) is dict:
                    compare(value_1, value_2, key_order)
                else:
                    yield {'key_order': deepcopy(key_order), 'change': 'updated', 'value': value_1, 'updated_value': value_2}
            else:
                yield {'key_order': deepcopy(key_order), 'change': 'same', 'value': value_1, 'updated_value': None}
        elif key in d1 and key not in d2:
            yield {'key_order': deepcopy(key_order), 'change': 'removed', 'value': value_1, 'updated_value': None}
        else:
            yield {'key_order': deepcopy(key_order), 'change': 'added', 'value': value_2, 'updated_value': None}


def uniformed(key_order: list = [], change: str = 'DEFAULT_CHANGE', value = None, updated_value = None) -> dict:
    return {'key_order': key_order, 'change': change, 'value': value, 'updated_value': updated_value}

def uniform(d1: dict = {}, d2: dict = {}) -> list:
    return list(compare(d1, d2))
    return list(map(uniformed, *compare(d1, d2)))

