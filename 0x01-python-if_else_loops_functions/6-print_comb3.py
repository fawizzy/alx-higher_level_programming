#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i < j:

            print("{:02d}".format((i*10) + j), end='')
            if int(str(i) + str(j)) != 89:
                print(end=', ')
print()
