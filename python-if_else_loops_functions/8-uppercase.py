#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase, followed by a newline."""
    for c in str:
        if 97 <= ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")
    print()
