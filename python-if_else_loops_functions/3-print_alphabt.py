#!/usr/bin/python3
dec = 97
while dec <= 122:
    print("{}".format(chr(dec)), end="")

    if dec == 101 | dec == 113:
        continue
    dec += 1