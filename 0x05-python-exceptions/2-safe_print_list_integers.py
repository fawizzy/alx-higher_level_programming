#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    no_of_int = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no_of_int += 1
        except TypeError:
            continue
        except ValueError:
            continue
        except IndexError:
            break
    print("")
    return (no_of_int)
