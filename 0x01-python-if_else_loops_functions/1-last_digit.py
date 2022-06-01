#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = (number * -1) % 10
else:
    lastdigit = number % 10
message = "Last digit of {} is {}"
if lastdigit > 5:
    print(message.format(number, lastdigit), "and is greater than 5")
elif lastdigit == 0:
    print(message.format(number, lastdigit), "and is 0")
elif lastdigit < 6 and lastdigit != 0:
    print(message.format(number, lastdigit), "and is less than 6 and not 0")
