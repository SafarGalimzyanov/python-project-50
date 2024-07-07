def check_value(value, style: str = ''):
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
    result += indent[2:] + '}'

    return result


def added_regular(key_order, value) -> str:
    indent = len(key_order) * ' '
    key = key_order[-1:]
    text = f'{indent[:-2]}+ {key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'


def removed_regular(key, value) -> str:
    indent = len(key_order) * ' '
    key = key_order[-1:]
    text = f'{indent[:-2]}- {key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'


def same_regular(key_order, value) -> str:
    indent = len(key_order) * ' '
    key = key_order[-1:]
    text = f'{indent}{key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'


def updated_regular(key_order, value, updated_value) -> str:
    indent = len(key_order) * ' '
    key = key_order[-1:]
    text = f'{indent}{key}'
    if type(value) is dict:
        return f'{text}{dict_to_str(value, indent)}\n'
    return f'{text}: {value}\n'

