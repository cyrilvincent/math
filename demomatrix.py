import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(mat1.shape) # Row first
print(mat1.size)
v1 = mat1.T.reshape(-1)
v1 = np.array([1,2,3,4])
mat1 = v1.reshape(-1,2)
print(mat1)
print(np.linalg.inv(mat1))
mat2 = mat1.T
print(mat1 * mat2)
print(np.dot(mat1, mat2))

print(mat1)
print(np.sum(mat1, axis=1))