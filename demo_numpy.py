import numpy as np

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(v1 * v2)
print(np.sin(v1))

print(v1.ndim)
print(v1.size)
print(v1.shape)
print(v1.dtype)

mat1 = np.array([[1,2], [3,4]])
print(mat1)
print(mat1.ndim)
print(mat1.size)
print(mat1.shape)
print(mat1.dtype)

print(v1 + mat1)