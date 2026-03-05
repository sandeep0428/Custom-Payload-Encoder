import random
import string

def random_insertion(payload):

    result = ""

    for char in payload:
        result += char
        result += random.choice(string.ascii_letters)

    return result


def split_and_concat(payload):

    parts = [payload[i:i+2] for i in range(0, len(payload), 2)]

    return " + ".join(f'"{p}"' for p in parts)


def escape_sequence(payload):

    return ''.join("\\x{:02x}".format(ord(c)) for c in payload)
