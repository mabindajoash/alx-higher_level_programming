#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_sum = 0
    total_sum = 0
    for value, weight in my_list:
        weighted_sum += value * weight
        total_sum += weight
    return weighted_sum / total_sum
