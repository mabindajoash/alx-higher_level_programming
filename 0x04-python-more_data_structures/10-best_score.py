#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    a = []
    for i, j in a_dictionary.items():
        a.append(j)
    a.sort()
    for key, value in a_dictionary.items():
        if value is a[-1]:
            return key

