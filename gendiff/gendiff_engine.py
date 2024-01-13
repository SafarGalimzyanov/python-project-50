from copy import deepcopy

def generate_depth(d1: dict, d2: dict={}) -> tuple:
    d1 = dict(sorted(d1.items()))
    d2 = dict(sorted(d2.items()))
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

def generate_tree(d1: dict, d2: dict={}) -> str:
    result = ''
    start = '{\n\n'
    end = '\n}'
    def inner(d1, d2, result):
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
        

    inner(d1, d2)
    return start + result + end

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
