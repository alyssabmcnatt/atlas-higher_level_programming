#!/usr/bin/python3
number = 0
while number <= 98:
    print("{0:02d}".format(number), end=", ")
    number += 1
    if number == 99:
        print("{0:02d}".format(number))
