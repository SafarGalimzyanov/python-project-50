def plain_added(key_order, value, updated_value) -> str:
    separate_string = '.'
    text = f"Property '{separate_string.join(key_order)}' was added with value: "

    if type(v2) is dict:
        return f'{text}[complex value]\n'
    return f'{text}{value}\n'


def plain_removed(key_order, value, updated_value) -> str:
    separate_string = '.'
    return f"Property '{separate_string.join(key_order)}' was removed"


def plain_same(key_order, value, updated_value) -> str:
    return ''


def plain_updated(key_order, value, updated_value) -> str:
    separate_string = '.'
    text = f"Property '{separate_string.join(key_order)}' was updated. From "

    if type(v1) is dict:
        return f'{text}[complex value] to {updated_value}\n'
    if type(v2) is dict:
        return f'{text}{value} to [complex value]\n'
    return f'{text}{value} to {updated_value}\n'


def plain(d: dict = {}) -> str:
    change = d.get('change')
    key_order = d.get('key_order')
    value = d.get('value')
    updated_value = d.get('updated_value') if 'updated_value' in d else None
    change_functions = {
            'added': plain_added,
            'removed': plain_removed,
            'same': plain_same,
            'updated': plain_updated
            }

    return change_functions.get(change)(key_order, value, updated_value)
