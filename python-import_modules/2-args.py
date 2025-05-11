#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name
    num_args = len(argv)

    # Print the number of arguments with proper formatting
    if num_args == 0:
        print("Number of argument(s):0")
    elif num_args == 1:
        print("Number of argument(s): 1 argument:")
    else:
        print(f"Number of argument(s): {num_args} arguments:")

    # Print each argument with its position if there are any arguments
    for i in range(num_args):
        print(f"{i + 1}: {argv[i]}")

if __name__ == "__main__":
    main()
