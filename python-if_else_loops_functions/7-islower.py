#!/usr/bin/python3
if not isinstance(c, str) or len(c) != 1:
    raise TypeError("Expected a single character")
def islower(c):
    if 'a' <= c <= 'z':
        return True
    return False
