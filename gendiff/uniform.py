def uniform(d1: dict = {}, d2: dict = {}) -> list:
    def append_(key, change: str, value, updated_value = None) -> dict:
        return {'key': key, 'change': change, 'value': value, 'updated_value': updated_value}

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

    result = []
    compare(d1, d2)
    return result
