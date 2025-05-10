#!/usr/bin/python3
# Import functions from calculator_1.py
from calculator_1 import calc 

if __name__ == "__main__":
    a = 10
    b = 5

    # Perform calculations
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
