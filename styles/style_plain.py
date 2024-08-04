SEPARATE_KEYS_STRING = '.'


def plain_added(key_order, value, updated_value: str = '') -> str:
    text = f"Property '{SEPARATE_KEYS_STRING.join(key_order)}' was added with value: "

    if type(updated_value) is dict:
        return f'{text}[complex value]\n'
    return f'{text}{value}\n'


def plain_removed(key_order, value, updated_value: str = '') -> str:
    return f"Property '{SEPARATE_KEYS_STRING.join(key_order)}' was removed"


def plain_same(key_order, value, updated_value) -> str:
    return ''


def plain_updated(key_order, value, updated_value: str = '') -> str:
    text = f"Property '{SEPARATE_KEYS_STRING.join(key_order)}' was updated. From "

    if type(value) is dict:
        return f'{text}[complex value] to {updated_value}\n'
    if type(updated_value) is dict:
        return f'{text}{value} to [complex value]\n'
    return f'{text}{value} to {updated_value}\n'


def plain(d: dict = {}, *args) -> str:
    change = d.get('change')
    key_order = d.get('key_order')
    value = d.get('value')
    updated_value = d.get('updated_value')
    change_functions = {
            'added': plain_added,
            'removed': plain_removed,
            'same': plain_same,
            'updated': plain_updated
            }

    return change_functions.get(change)(key_order, value, updated_value)
