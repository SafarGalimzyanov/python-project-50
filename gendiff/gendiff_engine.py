from copy import deepcopy
from stylish.stylize import added, removed, updated, dicts, different_dicts


#function to print dicts
def print_dict(d: dict={}, depth: int=0) -> str:
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

def print_diff(d1, d2, format_print: str, depth: int=4, space: int=2) -> str:
    result = ''
    keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
    
    indent = space*' '
    default = indent + '  '
    key_in_dict1 = indent + '- '
    key_in_dict2 = indent + '+ '
    dict_open = ': {'
    dict_close = indent + ' }'

    for key in keys:
        v1 = d1.get(key)
        key_v1 = f'{key}: {v1}'
        v2 = d2.get(key)
        key_v2 = f'{key}: {v2}'
        

        if key in d1 and key in d2: #same keys
            if type(v1) is dict and type(v2) is dict:
                if v1 != v2: #diff dicts = special case
                    result += different_dicts(indent, key, v1, v2, print_format)

                    .key('print_dict')(key, v1, v2) #передаем функции параметры
                    #аналогично для остальных
                    '''
                    print(f'{default}{key}{dict_open}')
                    print_diff(v1, v2, depth+4, space+4) #print result here
                    print(f'{dict_close}', end='')
                    result = ''  #finished -> next key
                    '''
                else:
                    result += same_value(indent, key, v1, print_format)
                    result = 
                    result = f'{default}{key}{print_dict(v1, depth+4)}' 
            else:
                if v1 != v2: #diff values -> show both
                    result += updated(indent, key, v1, v2, print_format)
                    result = 
                    result = f'{key_in_dict1}{key_v1}\n{key_in_dict2}{key_v2}'
                else: #same values -> show any
                    result += same_value(indent, key, v1, print_format)
                    result = 
                    result = f'{default}{key_v1}'
        elif key in d1 and key not in d2: #key in dict 1
            if type(v1) is dict: #dict -> print_dict()
                result += removed(indent, key, v1, print_format) #определяем, что словарь внутри функции
                result = 
                result = f'{key_in_dict1}{key}{print_dict(v1, depth+4)}'
            else:
                result += removed(indent, key, v1, print_format)
                result = 
                result = f'{key_in_dict1}{key_v1}'
        else: #key in dict 2
            if type(v2) is dict: #dict -> print_dict()
                result += added(indent, key, v2, print_format)
                result = 
                result = f'{key_in_dict2}{key}{print_dict(v2, depth+4)}'
            else:
                result += added(indent, key, v2, print_format)
                result = 
                result = f'{key_in_dict2}{key_v2}'

    return result


def generate_output(d1: dict={}, d2: dict={}, print_format: str='') -> str:
    print_format = stylize(print_format)
    print_diff(d1, d2) #main function
    
    return '' #only printing -> no return
