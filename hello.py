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

a = 3 # Scalar
l = [1,2,3] # List # Array # Vector # Serie
m = [[1,2],[3,4]] # Array # Matrix #Dataframe
# NDarray
print(len(m))