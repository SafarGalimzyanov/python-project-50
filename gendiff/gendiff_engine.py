from stylish.stylize import added, removed, updated, same


def compare_files(d1, d2, style: str, depth: int=4, space: int=2) -> str:
    result = ''
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))    
    indent = space*' '
    '''
    default = indent + '  '
    key_in_dict1 = indent + '- '
    key_in_dict2 = indent + '+ '
    dict_open = ': {'
    dict_close = indent + ' }'
    '''
    for key in keys:
        v1 = d1.get(key)
        key_v1 = f'{key}: {v1}'
        v2 = d2.get(key)
        key_v2 = f'{key}: {v2}'
        
        if key in d1 and key in d2: #same keys
            if type(v1) is dict and type(v2) is dict:
                if v1 != v2: #special
                    result += f'{indent}  {key}: "{"')
                    compare_files(v1, v2, style, depth+4, space+4)
                    result += f'{indent} "}"'
                else:
                    result += same(key, v1, style, depth, indent)
                    #result = f'{default}{key}{print_dict(v1, depth+4)}' 
            else:
                if v1 != v2:
                    result += updated(key, v1, v2, style, depth, indent)
                    #result = f'{key_in_dict1}{key_v1}\n{key_in_dict2}{key_v2}'
                else:
                    result += same(key, v1, style, depth, indent)
                    #result = f'{default}{key_v1}'
        elif key in d1 and key not in d2: #key in dict 1
            if type(v1) is dict:
                result += removed(key, v1, style, depth, indent)
                #result = f'{key_in_dict1}{key}{print_dict(v1, depth+4)}'
            else:
                result += removed(key, v1, style, depth, indent)
                #result = f'{key_in_dict1}{key_v1}'
        else:
            if type(v2) is dict: #dict -> print_dict()
                result += added(key, v2, style, depth, indent)
                #result = f'{key_in_dict2}{key}{print_dict(v2, depth+4)}'
            else:
                result += added(key, v2, style, depth, indent)
                #result = f'{key_in_dict2}{key_v2}'

    return result


def generate_diff(d1: dict={}, d2: dict={}, style: str='') -> str:
    return compare_files(d1, d2, style)
