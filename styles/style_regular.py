_NOT_PROVIDED = object()

DEFAULT_INDENT_LEN = 4
DEFAULT_INDENT = DEFAULT_INDENT_LEN * ' '
TEST_INDENT = '****'

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
    lp = len(prev_key_order)
    end_nested_indent = ''
    index = 0
    for index, (key, prev_key) in enumerate(zip(key_order, prev_key_order)):
        if key != prev_key:
            break
    for i in range(1, lp-index):
        end_nested_indent += f'{DEFAULT_INDENT*(len(prev_key_order)-i)}}}\n'
    
    start_nested_indent = ''
    for i in range(index, len(key_order)-1):
        start_nested_indent += f'{DEFAULT_INDENT*(i+1)}{key_order[i]}: {{\n'

    before_key_indent = DEFAULT_INDENT*len(key_order)

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
    indent = DEFAULT_INDENT*len(key_order)
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_removed(indent, key, value, updated_value, key_order) -> str:
    text = f'{indent[:-2]}- '
    indent = DEFAULT_INDENT*len(key_order)
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_same(indent, key, value, updated_value, key_order) -> str:
    text = f'{indent}'
    indent = DEFAULT_INDENT*len(key_order)
    if type(value) is dict:
        return f'{text}{key}: {{\n{dict_to_str(value, indent)}\n'
    return f'{text}{key}: {value}\n'


def regular_updated(indent, key, value, updated_value, key_order) -> str:
    text_removed = f'{indent[:-2]}- '
    text_added = DEFAULT_INDENT*len(key_order)
    text_added = text_added[:-2] + '+ '
    indent = DEFAULT_INDENT*len(key_order)
    if type(value) is dict:
        if type(updated_value) is dict:
            return f'{text_removed}{key}: {dict_to_str(value, indent)}\n{text_added}{key}: {dict_to_str(updated_value, indent)}\n'
        return f'{text_removed}{key}: {{\n{dict_to_str(value, indent)}\n{text_added}{key}: {updated_value}\n'
    elif type(updated_value) is dict:
        return f'{text_removed}{key}: {value}\n{text_added}{key}: {dict_to_str(updated_value, indent)}\n'
    else:
        return f'{text_removed}{key}: {value}\n{text_added}{key}: {updated_value}\n'


def regular(d: dict = {}, prev_key_order: list = []) -> str:
    if prev_key_order is _NOT_PROVIDED:
        prev_ley_order = []

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

    indent = get_nested_indent(key_order, prev_key_order)
    key = key_order[-1]
    return change_functions.get(change)(indent, key, check_value(value), check_value(updated_value), key_order)
