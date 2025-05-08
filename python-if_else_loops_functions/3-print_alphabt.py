#!/usr/bin/python3
print("{}".format(
    "".join(chr(c) for c in range(97, 123) if c != 113 and c != 101)
), end="")
