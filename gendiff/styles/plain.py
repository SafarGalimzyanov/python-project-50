def added(key_order, value, updated_value) -> str:
    separate_string = '.'
    text = f"Property '{separate_string.join(key_order)}' was added with value: "

    if type(v2) is dict:
        return f'{text}[complex value]\n'
    return f'{text}{value}\n'


def removed(key_order, value, updated_value) -> str:
    separate_string = '.'
    return f"Property '{separate_string.join(key_order)}' was removed"


def same(key_order, value, updated_value) -> str:
    return ''


def updated(key_order, value, updated_value) -> str:
    separate_string = '.'
    text = f"Property '{separate_string.join(key_order)}' was updated. From "

    if type(v1) is dict:
        return f'{text}[complex value] to {updated_value}\n'
    if type(v2) is dict:
        return f'{text}{value} to [complex value]\n'
    return f'{text}{value} to {updated_value}\n'


def plain(d: dict = {}) -> str:
    key_order, change, value, updated_value = d.values()
    change_functions = {
            'added': added,
            'removed': removed,
            'same': same,
            'updated': updated
            }

    return change_functions.get(change)(key_order, value, updated_value)
