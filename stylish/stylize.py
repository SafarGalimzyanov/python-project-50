def added(indent, depth, key, value_2, style: str='') -> str:
    if style == '--plain':
        if type(value_2) is dict:
            return '{key_in_dict2}{key}{print_dict(v2, depth+4)}'
        else:
            return '{key_in_dict2}{key_v2}'
    else:
        if type(value_2) is dict:
            return '{key_in_dict2}{key}{print_dict(v2, depth+4)}'
        else:
            return '{key_in_dict2}{key_v2}'




def removed(indent, key, value_1, value_2=0) -> str:
    if style == '--plain':
        if type(value_2) is dict:
            return '{key_in_dict1}{key}{print_dict(value_1, depth+4)}'
        else:
            return '{key_in_dict1}{key_v1}'
    else:
        if type(value_2) is dict:
            return '{key_in_dict1}{key}{print_dict(value_1, depth+4)}'
        else:
            return '{key_in_dict1}{key_v1}'
    return result

                result = f'{key_in_dict1}{key}{print_dict(v1, depth+4)}'
                result = f'{key_in_dict1}{key_v1}'



def updated(indent, key, value_1, value_2=0) -> str:
    if style == '--plain':
        if type(value_2) is dict:
            return '{key_in_dict2}{key}{print_dict(v2, depth+4)}'
        else:
            return '{key_in_dict2}{key_v2}'
    else:
        if type(value_2) is dict:
            return '{key_in_dict2}{key}{print_dict(v2, depth+4)}'
        else:
            return '{key_in_dict2}{key_v2}'
    return result
#not dicts
                    result += updated(indent, key, v1, v2, print_format)
                    result = f'{key_in_dict1}{key_v1}\n{key_in_dict2}{key_v2}'
print(f'{default}{key}{dict_open}')
                    print_diff(v1, v2, depth+4, space+4) #print result here
                    print(f'{dict_close}', end='')
                    result = ''  #finished -> next key
 



def same_value(indent, key, v1) -> str:
#dicts
                    result = f'{default}{key}{print_dict(v1, depth+4)}' 
                    result = f'{default}{key_v1}'


def stylize(format_flag: str='') -> dict:


    indent = space*' '
    default = indent + '  '
    key_in_dict1 = indent + '- '
    key_in_dict2 = indent + '+ '
    dict_open = ': {'
    dict_close = indent + ' }'




    def print_dict_plain(d: dict={}, depth: int=0) -> str:
        result = ': {\n'
        indent = depth*' '
        for key in d:
            v = d.get(key)
            key_v = f'{key}: {v}'
            if type(v) is dict:
                result += f'{indent}{key}{print_dict(v, depth+4)}\n'
            else:
                result += f'{indent}{key_v}\n'
        result += indent[4:] + '}'
        return result
    def print_dict_default(d: dict={}, depth: int=0) -> str:
        result = ': {\n'
        indent = depth*' '
        for key in d:
            v = d.get(key)
            key_v = f'{key}: {v}'
            if type(v) is dict:
                result += f'{indent}{key}{print_dict(v, depth+4)}\n'
            else:
                result += f'{indent}{key_v}\n'
        result += indent[4:] + '}'
        return result
