#!/usr/bin/python3
dec = 97
while dec <= 122:
    if dec == 101 or dec == 113:
        dec += 1
    else:
        print("{}".format(chr(dec)), end="")
        dec += 1
