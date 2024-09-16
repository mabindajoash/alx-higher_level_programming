#!/usr/bin/python3
def no_c(my_string):
    a = 0
    s = ""
    new_string = ""
    for i in my_string:
        if 'c' in my_string or 'C' in my_string:
            new_string = new_string + s[a:i]
            a = i + 1
    return new_string
