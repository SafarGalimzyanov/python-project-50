
def added_plain(key_order, value) -> str:
    separate_string = '.'
    text = f"Property '{separate_string.join(key)}' was added with value: "

    if type(v2) is dict:
        return f'{text}[complex value]\n'
    return f'{text}{value}\n'


def removed_plain(key_order, value) -> str:
    separate_string = '.'
    return f"Property '{separate_string.join(key)}' was removed"


def same_plain(key_order, value) -> str:
    return ''


def updated_plain(key_order, value, updated_value) -> str:
    separate_string = '.'
    text = f"Property '{separate_string.join(key_order)}' was updated. From "

    if type(v1) is dict:
        return f'{text}[complex value] to {updated_value}\n'
    if type(v2) is dict:
        return f'{text}{value} to [complex value]\n'
    return f'{text}{value} to {updated_value}\n'

