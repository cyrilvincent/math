import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(np.sum(mat1, axis=1))
print(mat1.shape)
print(mat1.reshape(4))

v1 = np.array([1,2,3,4,5,6])
mat2 = v1.reshape(-1,2)
print(mat2)

mat2 = np.array([[4,5],[6,7]])
print(np.dot(mat1, mat2))

