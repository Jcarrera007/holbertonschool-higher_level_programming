#!/usr/bin/python3
def uppercase(str):
    if not isinstance(str, str):
        raise TypeError("Expected a string")
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))