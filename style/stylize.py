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


def dict_to_str(d, depth) -> str:
    result = ': {\n'
    indent = depth*' '
    for key in d:
        v = d.get(key)
        v = check_value(v)
        key_v = f'{key}: {v}'

        if type(v) is dict:
            result += f'{indent}{key}{dict_to_str(v, depth+4)}\n'
        else:
            result += f'{indent}{key_v}\n'
    result += indent[4:] + '}'

    return result


def added(key, v2, style, depth, indent, ancestors) -> str:
    indent += '+ '
    key_v2 = f'{key}: {v2}'
    if style != 'plain':
        if type(v2) is dict:
            return f'{indent}{key}{dict_to_str(v2, depth+4)}\n'
        return f'{indent}{key_v2}\n'
    if type(v2) is dict:
        return f"Property '{ancestors[1:]}' was added with value: [complex value]\n"
    return f"Property '{ancestors[1:]}' was added with value: {v2}\n"


def removed(key, v1, style, depth, indent, ancestors) -> str:
    indent += '- '
    key_v1 = f'{key}: {v1}'

    if style != 'plain':
        if type(v1) is dict:
            return f'{indent}{key}{dict_to_str(v1, depth+4)}\n'
        return f'{indent}{key_v1}\n'
    if type(v1) is dict:
        return f"Property '{ancestors[1:]}' was removed\n"
    return f"Property '{ancestors[1:]}' was removed\n"


def updated(key, v1, v2, style, depth, indent, ancestors) -> str:
    indent1 = indent + '- '
    indent2 = indent + '+ '
    key_v1 = f'{key}: {v1}'
    key_v2 = f'{key}: {v2}'

    if style != 'plain':
        if type(v1) is dict:
            return f'{indent1}{key}{dict_to_str(v1, depth+4)}\n{indent2}{key_v2}\n'
        if type(v2) is dict:
            return f'{indent1}{key_v1}\n{indent2}{key}{dict_to_str(v2, depth+4)}\n'
        return f'{indent1}{key_v1}\n{indent2}{key_v2}\n'
    if type(v1) is dict:
        return f"Property '{ancestors[1:]}' was updated. From [complex value] to {v2}\n"
    if type(v2) is dict:
        return f"Property '{ancestors[1:]}' was updated. From {v1} to [complex value]\n"
    return f"Property '{ancestors[1:]}' was updated. From {v1} to {v2}\n"


def same(key, v1, style, depth, indent, ancestors) -> str:
    indent += '  '
    v1 = dict_to_str(v1, depth+4) if type(v1) is dict else v1
    key_v1 = f'{key}: {v1}'

    if style != 'plain':
        if type(v1) is dict:
            return f'{indent}{key}{dict_to_str(v1, depth+4)}\n'
        return f'{indent}{key_v1}\n'
    return ''


def get_result(params: tuple, change: str) -> str:
    key, v1, v2, style, depth, indent, ancestors = params
    v1, v2 = check_value(v1, style), check_value(v2, style)
    match change:
        case 'added':
            return added(key, v2, style, depth, indent, ancestors)
        case 'removed':
            return removed(key, v1, style, depth, indent, ancestors)
        case 'same':
            return same(key, v1, style, depth, indent, ancestors)
        case 'updated':
            return updated(key, v1, v2, style, depth, indent, ancestors)
