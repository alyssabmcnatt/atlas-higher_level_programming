#!/usr/bin/python3
dec = 97
while dec <= 122:
    if dec == 101 || dec == 113:
        continue
    print("{}".format(chr(dec)), end="")
    dec += 1