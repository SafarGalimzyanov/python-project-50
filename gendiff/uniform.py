from copy import deepcopy
from typing import Optional


def compare(d1: dict = {}, d2: dict = {}, key_order: Optional[list] = None):
    if key_order is None:
        key_order = []
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
    key_order.append(keys[0])
    for key in keys:
        value_1 = d1.get(key)
        value_2 = d2.get(key)
        key_order[-1] = key

        if key in d1 and key in d2:
            if value_1 != value_2:
                if isinstance(value_1, dict) and isinstance(value_2, dict):
                    yield from compare(value_1, value_2, deepcopy(key_order))
                else:
                    yield ('updated', deepcopy(key_order), value_1, value_2)
            else:
                yield ('same', deepcopy(key_order), value_1)
        elif key in d1 and key not in d2:
            yield ('removed', deepcopy(key_order), value_1)
        else:
            yield ('added', deepcopy(key_order), value_2)


def turn_to_dict(t) -> dict:
    change, key_order, value, *updated_value = t
    if not updated_value:
        return {'change': change, 'key_order': key_order, 'value': value}
    return {'change': change, 'key_order': key_order, 'value': value, 'updated_value': updated_value[0]}


def uniform(d1: dict = {}, d2: dict = {}) -> list:
    if not d1 and not d2:
        return []
    return [turn_to_dict(result) for result in list(compare(d1, d2))]
