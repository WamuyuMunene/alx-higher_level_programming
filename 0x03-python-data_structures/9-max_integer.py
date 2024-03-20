#!/usr/bin/python3
def max_integer(my_list=[]):
    max = sorted(my_list, reverse = True)
    if len(my_list) == 0:
        return None
    else:
        return max[0]
