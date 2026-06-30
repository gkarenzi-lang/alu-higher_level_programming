#!/usr/bin/python3
def print_last_digit(number):
    """Print (no newline) and return the last digit of number."""
    last_digit = number - (int(number / 10) * 10)
    print("{:d}".format(abs(last_digit)), end="")
    return last_digit
