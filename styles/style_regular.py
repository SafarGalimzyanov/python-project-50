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


def get_indent(key_order: list, previous_key_order: list = []) -> str:
    def get_index(l1: list, l2: list) -> int:
        index = -1
        try:
            while l1[index + 1] == l2[index + 1]:
                index += 1
        except IndexError:
            return index
        return index

    def get_previous_indent(index: int, l: list) -> str:
        ...


    def get_current_indent(index: int, l: list) -> str:
        space_indent = 4 * ' '
        indent = space_indent
        if index > -1:
            indent += space_indent * (index + 1)
            space_indent += DEFAULT_INDENT * (index + 1)
            for i in range(index+1, len(l)-1):
                space_indent += DEFAULT_INDENT
                indent += f'{l[i]}: {{\n{space_indent}'
        elif index == -1 and len(l) > 1:
            for i in range(len(l)):
                space_indent += 4 * ' '
                indent += f'{l[i]}: {{\n{space_indent}'

        return indent

    index = get_index(key_order, previous_key_order)
    current_indent = get_current_indent(index, key_order)
    
    return current_indent + ''
    return f'index: {index}{current_indent}'

def dict_to_str(d: dict = {}, indent: str = '') -> str:
    result = ''
    indent += DEFAULT_INDENT
    for key, value in d.items():
        value = check_value(value)
        if type(value) is dict:
            result += f'{indent}{key}: {{\n{dict_to_str(value, indent)}\n'
        else:
            result += f'{indent}{key}: {value}\n'

    result += indent[:-DEFAULT_INDENT_LEN] + '}'

    return result


def regular_added(indent, key, value, updated_value) -> str:
    text = f'{indent[:-2]}+ '
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_removed(indent, key, value, updated_value) -> str:
    text = f'{indent[:-2]}- '
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_same(indent, key, value, updated_value) -> str:
    text = f'{indent}'
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_updated(indent, key, value, updated_value) -> str:
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

    indent = get_indent(key_order, previous_key_order)
    key = key_order[-1]
    return change_functions.get(change)(indent, key, value, updated_value)
