def check_value(value):
    match value:
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'


def dict_to_str(d: dict, indent: str) -> str:
    result = ': {\n'
    indent += 4 * ' '
    for key in d:
        value = check_value(d.get(key))

        if type(value) is dict:
            result += f'{indent}  {key}{dict_to_str(value, indent)}\n'
        else:
            result += f'{indent}  {key}: {value}\n'
    result += indent[4:] + '}'

    return result


def added(indent, key, value, updated_value) -> str:
    text = f'{indent[:-2]}+ {key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'


def removed(indent, key, value, updated_value) -> str:
    text = f'{indent[:-2]}- {key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'


def same(indent, key, value, updated_value) -> str:
    text = f'{indent}{key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'


def updated(indent, key, value, updated_value) -> str:
    text = f'{indent}{key}'
    return f'{removed(indent, key, value, None}\n{added(indent, key, None, updated_value}\n'


def regular(d: dict = {}) -> str:
    key_order, change, value, updated_value = d.values()
    change_functions = {
            'added': added,
            'removed': removed,
            'same': same,
            'updated': updated
            }
    indent = len(key_order) * ' '
    key = key_order[-1:]

    return change_functions.get(change)(indent, key, value, updated_value)
