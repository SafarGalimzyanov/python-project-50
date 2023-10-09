#!/usr/bin/env python3


from typing import TextIO


def diff_json(first_file: TextIO, second_file: TextIO) -> str:
    result = ''
    
    with open(first_file, 'r') as f1, open(second_file, 'r') as f2:
        arr1 = f1.readlines()
        arr2 = f2.readlines()
        

        dict1, dict2 = dict(), dict()

        for i in range(len(arr1)):
            k, v = arr1[i].split(':')
            dict1.update({k: v})
        for i in range(len(arr2)):
            k, v = arr2[i].split(':')
            dict2.update({k: v})
        
        
        dict_in1_in2 = dict()

        for key in dict1:
            if key in dict2 and dict1.get(key) == dict2.get(key):
                dict_in1_in2.update(d)
                dict1.pop(key)
                dict2.pop(key) 

        dict_result = dict()
        dict_result.update(dict1)
        dict_result.update(dict_in1_in2)
        dict_result.update(dict2)

        for key in dict_result:
            d = {key: dict_result.get(key)}
            if key in dict1:
                result += f'  - {d}'
            if key in dict2:
                result += f'  + {d}'
            
            result += f'    {d}'
            

    return result
