#!/usr/bin/python3
def no_c(my_string):
    copy_str = my_string.translate({ord(c): None for c in 'cC'})
    return ("".join(copy_str))
