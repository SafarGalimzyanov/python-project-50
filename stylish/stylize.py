def check_value(v, style: str=''):
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
    result = ": {\n"
    indent = depth*" "
    for key in d:
        v = d.get(key)
        v = check_value(v)

        key_v = f"{key}: {v}"
        if type(v) is dict:
            result += f"{indent}{key}{dict_to_str(v, depth+4)}\n"
        else:
            result += f"{indent}{key_v}\n"
    result += indent[4:] + "}"
    return result


def added(key, v2, style, depth, indent, ancestors) -> str:
    key_in_dict2 = indent + "+ "
    #if type(v2) is str:
        #v2 = f"'{v2}'"
    v2 = check_value(v2, style)

    key_v2 = f"{key}: {v2}"

    if style != "plain":
        if type(v2) is dict:
            return f"{key_in_dict2}{key}{dict_to_str(v2, depth+4)}\n"
        else:
            return f"{key_in_dict2}{key_v2}\n"
    else:
        if type(v2) is dict:
            return f"Property '{ancestors[1:]}' was added with value: [complex value]\n"
        else:
            return f"Property '{ancestors[1:]}' was added with value: {v2}\n"


def removed(key, v1, style, depth, indent, ancestors) -> str:
    key_in_dict1 = indent + "- "
    v1 = check_value(v1)

    key_v1 = f"{key}: {v1}"

    if style != "plain":
        if type(v1) is dict:
            return f"{key_in_dict1}{key}{dict_to_str(v1, depth+4)}\n"
        else:
            return f"{key_in_dict1}{key_v1}\n"
    else:
        if type(v1) is dict:
            return f"Property '{ancestors[1:]}' was removed\n"
        else:
            return f"Property '{ancestors[1:]}' was removed\n"


def updated(key, v1, v2, style, depth, indent, ancestors) -> str:
    key_in_dict1 = indent + "- "
    key_in_dict2 = indent + "+ "
    #if type(v1) is str:
    #    v1 = f"'{v1}'"
    #if type(v2) is str:
    #    v2 = f"'{v2}'"
    v1 = check_value(v1, style)
    v2 = check_value(v2, style)

    key_v1 = f"{key}: {v1}"
    key_v2 = f"{key}: {v2}"

    if style != "plain":
        if type(v1) is dict:
            return f"{key_in_dict1}{key}{dict_to_str(v1, depth+4)}\n{key_in_dict2}{key_v2}\n"
        elif type(v2) is dict:
            return f"{key_in_dict1}{key_v1}\n{key_in_dict2}{key}{dict_to_str(v2, depth+4)}\n"
        else:
            return f"{key_in_dict1}{key_v1}\n{key_in_dict2}{key_v2}\n"
    else:
        if type(v1) is dict:
            return f"Property '{ancestors[1:]}' was updated. From [complex value] to {v2}\n"
        elif type(v2) is dict:
            return f"Property '{ancestors[1:]}' was updated. From {v1} to [complex value]\n"
        else:
            return f"Property '{ancestors[1:]}' was updated. From {v1} to {v2}\n"



def same(key, v1, style, depth, indent, ancestors) -> str:
    default = indent + "  "
    v1 = check_value(v1)

    key_v1 = f"{key}: {v1}"
    if style != "plain":
        if type(v1) is dict:
            return f"{default}{key}{dict_to_str(v1, depth+4)}\n"
        else:
            return f"{default}{key_v1}\n"
    else:
        if type(v1) is dict:
            return ""
        else:
            return ""
