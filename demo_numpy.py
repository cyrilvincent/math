import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4])
a2 = np.arange(8,12)
print(a1)
print(a2)
a3 = a1 + a2
print(a3)
a4 = a1 * a2
print(a4)
print(np.tanh(a1))

print(np.sum(np.tanh(a1)))

print(a1.ndim)
print(a1.size)
print(a1.shape)
print(a1.dtype)

x1 = [1,9,-8,5,7,99,45,66]
print(x1[::2])