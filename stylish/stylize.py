def dict_to_str(d, depth) -> str:
    result = ': {\n'
    indent = depth*' '
    for key in d:
        v = d.get(key)
        key_v = f'{key}: {v}'
        if type(v) is dict:
            result += f'{indent}{key}{dict_to_str(v, depth+4)}\n'
        else:
            result += f'{indent}{key_v}\n'
    result += indent[4:] + '}'
    return result


def added(key, v2, style, depth, indent) -> str:
    key_in_dict2 = indent + '+ '
    key_v2 = f'{key}: {v2}'

    if style == '--plain':
        if type(value_2) is dict:
            return '{key_in_dict2}{key}{dict_to_str(v2, depth+4)}'
        else:
            return '{key_in_dict2}{key_v2}'
    else:
        if type(value_2) is dict:
            return '{key_in_dict2}{key}{dict_to_str(v2, depth+4)}'
        else:
            return '{key_in_dict2}{key_v2}'




def removed(key, v1, style, depth, indent) -> str:
    key_in_dict1 = indent + '- '
    key_v1 = f'{key}: {v1}'

    if style == '--plain':
        if type(value_2) is dict:
            return f'{key_in_dict1}{key}{dict_to_str(value_1, depth+4)}'
        else:
            return f'{key_in_dict1}{key_v1}'
    else:
        if type(value_2) is dict:
            return f'{key_in_dict1}{key}{dict_to_str(value_1, depth+4)}'
        else:
            return f'{key_in_dict1}{key_v1}'


def updated(key, v1, v2, style, depth, indent) -> str:
    key_in_dict1 = indent + '- '
    key_in_dict2 = indent + '+ '
    key_v1 = f'{key}: {v1}'
    key_v2 = f'{key}: {v2}'

    if style == '--plain':
        return f'{key_in_dict1}{key_v1}\n{key_in_dict2}{key_v2}'
    else:
        return f'{key_in_dict1}{key_v1}\n{key_in_dict2}{key_v2}'


def same(key, v1, style, depth, indent) -> str:
    default = indent + '  '
    key_v1 = f'{key}: {v1}'

    if style == '--plain':
        if type(value_2) is dict:
            return f'{default}{key}{dict_to_str(v1, depth+4)}'
        else:
            return f'{default}{key_v1}'
    else:
        if type(value_2) is dict:
            return f'{default}{key}{dict_to_str(v2, depth+4)}'
        else:
            return f'{default}{key_v1}'


def stylize(format_flag: str='') -> dict:
???
    '''
    #INDENT
    indent = space*' '
    default = indent + '  '
    key_in_dict1 = indent + '- '
    key_in_dict2 = indent + '+ '
    '''
