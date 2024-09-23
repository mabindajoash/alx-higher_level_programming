#!/usr/bin/python3
def element_at(my_list, idx):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list):
=======
    if idx < 0 or idx >= len(my_list):
>>>>>>> 6f43b48bf2315000186847abdf6b2c9eec8942d2
        return None
    return my_list[idx]
