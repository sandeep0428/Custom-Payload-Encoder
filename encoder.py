import base64

def base64_encode(payload):
    return base64.b64encode(payload.encode()).decode()


def base64_decode(payload):
    return base64.b64decode(payload.encode()).decode()


def xor_encode(payload, key):
    return ''.join(chr(ord(c) ^ key) for c in payload)


def xor_decode(payload, key):
    return ''.join(chr(ord(c) ^ key) for c in payload)


def rot13_encode(payload):

    result = ""

    for char in payload:

        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))

        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))

        else:
            result += char

    return result
