import numpy as np

a1 = np.array([[1,2],[3,4]])
print(a1)
print(np.sum(a1))
print(np.sum(a1, axis=0))
print(np.sum(a1, axis=1))

# f(x) = 2.5x + 3
print(a1 * 2.5 + 3)

def f(x):
    return 2.5 * x + 3

g = lambda x: 2.5 * x + 3

def transform(l, array):
    return l(array)

print(f(a1))
print(g(a1))
print(transform(lambda x: 2.5 * x + 3, a1))

