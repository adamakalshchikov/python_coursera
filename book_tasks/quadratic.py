import sys
import cmath
import math

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("Zero not allowed. Enter another value")
                x = None
        except ValueError as err:
            print(err)
    return x


