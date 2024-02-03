from copy import deepcopy

def generate_depth(d1: dict, d2: dict={}) -> tuple:
    d1 = dict(sorted(d1.items()))
    d2 = dict(sorted(d2.items()))
'''
    def inner(d, depth: int=0):
        if d is dict:
            for key in d.keys():
                if d.get(key) is dict:
                    inner(d.get(key), depth + 4)
                d.update({key: (d.get(key), depth)
        else:
            return 0

    map(inner, d1, d2)
    return (d1, d2)
'''
def generate_output(d1: dict={}, d2: dict={}) -> str:
    depth = 4
    indent = 2
    print(f'type: {type(d1)}')
    def print_dict(d: dict={}, depth: int=0) -> str:
        result = ': {\n'
        space = depth*' '
        for key in d:
            v = d.get(key)
            if type(v) is dict:
                result += space + f'{key}{print_dict(v, depth+4)}\n'
            else:
                result += space + f'{key}: {d.get(key)}\n'
        result += space[4:] + '}'
        return result

    def inner(d1, d2, depth: int=4, indent: int=2):
        result = ''
        d1 = dict(d1)
        d2 = dict(d2)
        keys = sorted(tuple(set(d1.keys()).union(set(d2.keys()))))
        space = indent*' '
        for key in keys:
            v1 = d1.get(key)
            v2 = d2.get(key)
            if key in d1 and key in d2:
                if type(v1) is dict and type(v2) is dict:
                    if v1 != v2:
                        print(f'{space}  {key}:' + ' {')
                        inner(v1, v2, depth+4, indent+4) #словари не совпали
                        print(space + '  }', end='')
                        result = '' #очистка от последнего результата
                    else:
                        result = f'{space}  {key}{print_dict(v1, depth+4)}' 
                else:
                    if v1 != v2:
                        result = f'{space}- {key}: {v1}\n{space}+ {key}: {v2}'
                    else:
                        result = f'{space}  {key}: {v1}'
            elif key in d1 and key not in d2:
                if type(v1) is dict:
                    result = f'{space}- {key}{print_dict(v1, depth+4)}'
                else:
                    result = f'{space}- {key}: {v1}'
            else:
                if type(v2) is dict:
                    result = f'{space}+ {key}{print_dict(v2, depth+4)}'
                else:
                    result = f'{space}+ {key}: {v2}'
            print(result)
    inner(d1, d2)
    return ''
'''
        d_in1_in2, d_in1, d_in2, d_check = dict(), dict(), dict(), dict()
        for key in d2:
            if key not in d1:
                d_in2.update({key: d2.get(key)})

        for key in d1:
            d = {key: d1.get(key)}
            if key not in d2:
                d_in1.update(d)
            elif d1.get(key) == d2.get(key):
                d_in1_in2.update(d)
            else:
                d_check.update(d)

        for key in d_check:

        keys = set(d_in1_in2.keys())
        keys.update(set(d_in1.keys()))
        keys.update(set(d2.keys()))

        for key in sorted(keys):
            if key in d_in1:
                result += f'  - {key}: {d_in1.get(key)}\n'
            if key in d2:
                result += f'  + {key}: {d2.get(key)}\n'
            if key in d_in1_in2:
                result += f'    {key}: {d_in1_in2.get(key)}\n'
             
'''


def generate_diff(d1: dict, d2: dict={}) -> str:
    d_in1_in2, d_in1 = dict(), dict()
    for key in d1:
        d = {key: d1.get(key)}
        if d1.get(key) == d2.get(key):
            d_in1_in2.update(d)
            d2.pop(key)
        else:
            d_in1.update(d)

    keys = set(d_in1_in2.keys())
    keys.update(set(d_in1.keys()))
    keys.update(set(d2.keys()))

    start = '{\n\n'
    end = '\n}'
    result = ''
    for key in sorted(keys):
        if key in d_in1:
            result += f'  - {key}: {d_in1.get(key)}\n'
        if key in d2:
            result += f'  + {key}: {d2.get(key)}\n'
        if key in d_in1_in2:
            result += f'    {key}: {d_in1_in2.get(key)}\n'
 
    return start + result + end
