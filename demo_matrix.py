import numpy as np
v1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(v1, v1.shape)
mat1 = v1.reshape(-1, 4)
print(mat1, mat1.shape)
v2 = mat1.reshape(mat1.shape[0] * mat1.shape[1])
print(v2)
cube1 = mat1.reshape(2, -1, 3)
print(cube1)

mat3 = np.array([[1,2],[3,4]])
print(mat3)
print(np.sum(mat3, axis=1))