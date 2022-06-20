import sys
import numpy as np

def inc(i:int) -> int:
    return i+1


inc(3)
print("Hello World!")
print(sys.version)
print(np.__version__)
i = 0
while i < 10:
    print(f"i={i}")
    i = inc(i)