#!/usr/bin/python3
def print_last_digit(number):
    c = abs(number) % 10
    if number < 0:
        c = -c
    return c
