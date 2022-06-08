#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_test = set(my_list)

    for i in uniq_test:
        sum += i
    return sum
