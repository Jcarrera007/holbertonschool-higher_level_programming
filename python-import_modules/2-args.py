#!/usr/bin/python3


import sys


def main():
    args = sys.argv[1:]
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print each argument with its position
    for index, arg in enumerate(args, start=1):
        print(f"{index}: {arg}")


if __name__ == "__main__":
    main()
