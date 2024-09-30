#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    lenght = 0
    for i in my_list:
        lenght += 1
    try:
        if x > lenght:
            raise IndexError
        for i in my_list:
            if counter < x:
                print("{:d}".format(i), end="")
                counter += 1
        print()
        return counter
    except Exception:
        pass
    except IndexError:
        print("IndexError: list index out of range")
