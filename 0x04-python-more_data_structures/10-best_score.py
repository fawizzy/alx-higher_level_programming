#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values_list = list(a_dictionary.values())
        keys_list = list(a_dictionary.keys())
        max_value = max(values_list)
        max_key = keys_list[values_list.index(max_value)]
        return max_key
    return None
