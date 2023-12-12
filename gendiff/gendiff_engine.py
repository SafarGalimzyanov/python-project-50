def generate_diff(d1: dict, d2: dict) -> str:
    d_in1_in2, d_in1 = dict(), dict()
    for key in d1:
        d = {key: d1.get(key)}
        if d1.get(key) == d2.get(key):
            d_in1_in2.update(d)
            d2.pop(key)
        else:
            d_in1.update(d)

    keys = sorted(list(d_in1_in2.keys()) + list(d_in1.keys()) + list(d2.keys()))
    start = '{\n\n'
    end = '\n}'
    result = ''
    for key in keys:
        if key in d_in1:
            result += f'  - {key}: {d_in1.get(key)}\n'
        elif key in d2:
            result += f'  + {key}: {d2.get(key)}\n'
        else:
            result += f'    {key}: {d_in1_in2.get(key)}\n'
            
    return start + result + end
