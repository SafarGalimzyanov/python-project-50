def added(indent, key, value_1, value_2=0, style: str='') -> str:
    


                result = f'{key_in_dict2}{key_v2}'
                result = f'{key_in_dict2}{key}{print_dict(v2, depth+4)}'

    if style == '':
        return ...
    else:
        return ...


def removed(indent, key, value_1, value_2=0) -> str:
    return result

                result = f'{key_in_dict1}{key}{print_dict(v1, depth+4)}'
                result = f'{key_in_dict1}{key_v1}'

def updated(indent, key, value_1, value_2=0) -> str:
    return result
#not dicts
                    result += updated(indent, key, v1, v2, print_format)
#dicts
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
    
    indent = space*' '
    default = indent + '  '
    key_in_dict1 = indent + '- '
    key_in_dict2 = indent + '+ '
    dict_open = ': {'
    dict_close = indent + ' }'

    key_in12_same_values_default = '    '
    key_in12_diff_complex_values_default = ...
    key_in2_default = '  + '
    key_in1_default = '  - '
    
    key_in12_same_values_plain = '    '
    key_in12_diff_complex_values_plain = ...
    key_in2_plain = '  + '
    key_in1_plain = '  - '
    #случай одних key и разных value это key_in2 и key_in1
    if format_flag is '--plain':
        return {
        'key_in12_same_values': key_in12_same_values_default,
        'key_in12_diff_complex_values': key_in12_diff_complex_values_default,
        'key_in2': key_in2_default,
        'key_in1': key_in1_default,
        'print_dict': print_dict_default
        }
    else:
        return {
        'key_in12_same_values': key_in12_same_values_plain,
        'key_in12_diff_complex_values': key_in12_diff_complex_values_plain,
        'key_in2': key_in2_plain,
        'key_in1': key_in1_plain,
        'print_dict': print_dict_plain
        }
