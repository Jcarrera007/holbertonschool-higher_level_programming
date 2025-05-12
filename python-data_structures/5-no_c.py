#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char == 'c' or char == 'C':
            return my_string.replace('c', '').replace('C', '')
