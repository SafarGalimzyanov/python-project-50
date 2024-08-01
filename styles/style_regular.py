DEFAULT_INDENT_LEN = 4
DEFAULT_INDENT = DEFAULT_INDENT_LEN * ' '

def check_value(value):
    match value:
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'
        case _:
            return value


def get_nested_indent(key_order: list, prev_key_order: list) -> int:
    end_nested_indent = ''
    for i, (key, prev_key) in enumerate(zip(key_order, prev_key_order)):
        if key != prev_key:
            return str(i) + DEFAULT_INDENT
        #вот тут добавляем закрывающую скобку
        end_nested_indent += DEFAULT_INDENT * (len(prev_key_order) - i)

    start_nested_indent = ''
    for i, key in enumerate(key_order[-1]):
        start_nested_indent += f'{DEFAUL_INDENT*i}{key}: {\n'

    before_key_indent = DEFAULT_INDENT * len(key_order)

    return end_nested_indent + start_nested_indent + before_key_indent
    

def dict_to_str(d: dict = {}, indent: str = '') -> str:
    result = ''
    indent += f'{DEFAULT_INDENT}'
    for key, value in d.items():
        value = check_value(value)
        if type(value) is dict:
            result += f'{indent}{key}: {{\n{dict_to_str(value, indent)}\n'
        else:
            result += f'{indent}{key}: {value}\n'

    result += indent[:-DEFAULT_INDENT_LEN] + '}'

    return result


def regular_added(indent, key, value, updated_value, key_order) -> str:
    text = f'{indent[:-2]}+ '
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_removed(indent, key, value, updated_value, key_order) -> str:
    text = f'{indent[:-2]}- '
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_same(indent, key, value, updated_value, key_order) -> str:
    text = f'{indent}'
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_updated(indent, key, value, updated_value) -> str:
    text = f'{indent[:-2]}- '
    if type(value) is dict:
        if type(updated_value) is dict:
            return f'{text}{key}: {dict_to_str(value, indent)}\n{space_indent}+ {key}: {dict_to_str(updated_value, indent)}\n'
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n{space_indent}+ {key}: {updated_value}\n'
    elif type(updated_value) is dict:
        return f'{text}{key}: {value}\n{space_indent}+ {key}: {dict_to_str(updated_value, indent)}\n'
    else:
        return f'{text}{key}: {value}\n{space_indent}+ {key}: {updated_value}\n'

    return f'{regular_removed(indent, key, value, None)}{regular_added(indent, key, None, updated_value)}'


def regular(d: dict = {}, previous_key_order: list = []) -> str:
    change = d.get('change')
    key_order = d.get('key_order')
    value = d.get('value')
    updated_value = d.get('updated_value') if 'updated_value' in d else None

    change_functions = {
            'added': regular_added,
            'removed': regular_removed,
            'same': regular_same,
            'updated': regular_updated
            }

    indent = get_nested_indent(key_order, previous_key_order)
    key = key_order[-1]
    return change_functions.get(change)(indent, key, check_value(value), updated_value)
