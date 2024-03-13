ADDED = '+ '
REMOVED = '- '
SAME = '  '
DEF_INDENT = 4*' '

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
    key_v2 = f'{key}: {v2}'

    if style != 'plain':
        if type(v2) is dict:
            return f'{indent}{ADDED}{key}{dict_to_str(v2, indent)}\n'
        return f'{indent}{ADDED}{key_v2}\n'
    if type(v2) is dict:
        return f"Property '{ancestors[1:]}' was added with value: [complex value]\n"
    return f"Property '{ancestors[1:]}' was added with value: {v2}\n"


def removed(key, v1, style, indent, ancestors) -> str:
    key_v1 = f'{key}: {v1}'

    if style != 'plain':
        if type(v1) is dict:
            return f'{indent}{REMOVED}{key}{dict_to_str(v1, indent)}\n'
        return f'{indent}{REMOVED}{key_v1}\n'
    return f"Property '{ancestors[1:]}' was removed\n"


def updated(key, v1, v2, style, indent, ancestors) -> str:
    key_v1 = f'{key}: {v1}'
    key_v2 = f'{key}: {v2}'

    if style != 'plain':
        if type(v1) is dict:
            return f'{indent}{REMOVED}{key}{dict_to_str(v1, indent)}\n{indent}{ADDED}{key_v2}\n'
        if type(v2) is dict:
            return f'{indent}{REMOVED}{key_v1}\n{indent}{ADDED}{key}{dict_to_str(v2, indent)}\n'
        return f'{indent}{REMOVED}{key_v1}\n{indent}{ADDED}{key_v2}\n'
    if type(v1) is dict:
        return f"Property '{ancestors[1:]}' was updated. From [complex value] to {v2}\n"
    if type(v2) is dict:
        return f"Property '{ancestors[1:]}' was updated. From {v1} to [complex value]\n"
    return f"Property '{ancestors[1:]}' was updated. From {v1} to {v2}\n"


def same(key, v1, style, indent, ancestors) -> str:
    key_v1 = f'{key}: {v1}'

    if style != 'plain':
        if type(v1) is dict:
            return f'{indent}{SAME}{key}{dict_to_str(v1, indent)}\n'
        return f'{indent}{SAME}{key_v1}\n'
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
