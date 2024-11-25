import sys
import numpy as np
print("Hello")
print(sys.version)
print(np.__version__)

a1 = np.array([0,1,2,3,4,5,6,7,8,9])
a2 = np.arange(10)
print(a2)
for value in a2:
    if value % 2 == 0:
        print(value)

def add(x, y):
    return x + y

print(add(2,3))

def is_prime(x):
    if x < 2:
        return False
    for div in range(2, x):
        if x % div == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(7919))

a3 = np.arange(0,10,0.01)
print(a3)
a4 = np.linspace(0,10, 101)
print(a4)

a5 = np.random.rand(10)
print(a5)
a6 = np.random.randint(0,100,10)
print(a6)

a7 = np.array([1,2,3,4])
a8 = np.array([5,6,7,8])
a7 = a7.astype(np.float64)
a9 = a7 * a8
print(a9)




