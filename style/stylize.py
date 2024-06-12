ADDED = '+ '
REMOVED = '- '
SAME = '  '
DEF_INDENT = 4 * ' '


def check_value(v, style: str = ''):
    if style == 'plain' and type(v) is str:
        v = f"'{v}'"
    match v:
        case None:
            v = 'null'
        case True:
            v = 'true'
        case False:
            v = 'false'

    return v


def dict_to_str(d: dict, indent: str) -> str:
    result = ': {\n'
    indent += DEF_INDENT
    for key in d:
        v = d.get(key)
        v = check_value(v)
        key_v = f'{key}: {v}'

        if type(v) is dict:
            result += f'{indent}  {key}{dict_to_str(v, indent)}\n'
        else:
            result += f'{indent}  {key_v}\n'
    result += indent[2:] + '}'

    return result


def added(key, v2, style, indent, ancestors) -> str:
    default = f'{indent}{ADDED}{key}'
    plain = f"Property '{ancestors[1:]}' was added with value: "

    if style != 'plain':
        if type(v2) is dict:
            return f'{default}{dict_to_str(v2, indent)}\n'
        return f'{default}: {v2}\n'
    if type(v2) is dict:
        return f'{plain}[complex value]\n'
    return f'{plain}{v2}\n'


def removed(key, v1, style, indent, ancestors) -> str:
    default = f'{indent}{REMOVED}{key}'
    plain = f"Property '{ancestors[1:]}' was removed"

    if style != 'plain':
        if type(v1) is dict:
            return f'{default}{dict_to_str(v1, indent)}\n'
        return f'{default}: {v1}\n'
    return f'{plain}\n'


def updated(key, v1, v2, style, indent, ancestors) -> str:
    default_removed = f'{indent}{REMOVED}{key}'
    default_added = f'{indent}{ADDED}{key}'
    plain = f"Property '{ancestors[1:]}' was updated. From "

    if style != 'plain':
        if type(v1) is dict:
            return f'{default_removed}{dict_to_str(v1, indent)}\n{default_added}: {v2}\n'
        if type(v2) is dict:
            return f'{default_removed}: {v1}\n{default_added}{dict_to_str(v2, indent)}\n'
        return f'{default_removed}: {v1}\n{default_added}: {v2}\n'
    if type(v1) is dict:
        return f'{plain}[complex value] to {v2}\n'
    if type(v2) is dict:
        return f'{plain}{v1} to [complex value]\n'
    return f'{plain}{v1} to {v2}\n'


def same(key, v1, style, indent, ancestors) -> str:
    default = f'{indent}{SAME}{key}'
    if style != 'plain':
        if type(v1) is dict:
            return f'{default}{dict_to_str(v1, indent)}\n'
        return f'{default}: {v1}\n'
    return ''


def get_result(params: tuple, change: str) -> str:
    key, v1, v2, style, indent, ancestors = params
    v1, v2 = check_value(v1, style), check_value(v2, style)
    match change:
        case 'added':
            return added(key, v2, style, indent, ancestors)
        case 'removed':
            return removed(key, v1, style, indent, ancestors)
        case 'same':
            return same(key, v1, style, indent, ancestors)
        case 'updated':
            return updated(key, v1, v2, style, indent, ancestors)
