#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in my_list:
            if counter < x:
                print("{}".format(i), end="")
                counter += 1
    except IndexError:
        print("index error")
    finally:
        print()
        return counter
