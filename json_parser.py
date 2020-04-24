def write_key(key):
    if isinstance(key, (int, str, float, bool)):
        return '"' + str(key).lower() + '"'
    elif isinstance(key, type(None)):
        return '"' + "null" + '"'
    else:
        raise TypeError("keys must be str, int, float, bool or None, not " + str(type(key)))


def to_json(obj):
    current_json = ""
    if isinstance(obj, dict):

        current_json += '{'
        is_begin = True

        for key, value in obj.items():

            if not is_begin:
                current_json += ', '
            else:
                is_begin = False

            current_json += write_key(key)
            current_json += ": "
            current_json += to_json(value)

        current_json += '}'
    elif isinstance(obj, (tuple, list)):
        current_json += '['

        is_begin = True
        for value in obj:

            if not is_begin:
                current_json += ', '
            else:
                is_begin = False

            current_json += to_json(value)

        current_json += ']'

    elif isinstance(obj, str):
        current_json += '"' + obj + '"'
    elif isinstance(obj, (int, float, bool)):
        current_json += str(obj).lower()
    elif isinstance(obj, type(None)):
        current_json += "null"
    else:
        raise TypeError(str(type(obj)) + " cannot converted to json format")

    return current_json
