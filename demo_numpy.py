import numpy as np

a1 = np.arange(2, 10, 2)
print(a1)


print(np.random.randint(0,100))

a2 = np.array([1,2,3])
a3 = np.array([4,5,6])
print(a2.ndim, a2.size, a2.shape, a2.dtype)

m1 = np.array([[1,2],[3,4]])
print(m1.ndim, m1.size, m1.shape, m1.dtype)

print(a3 * a2)