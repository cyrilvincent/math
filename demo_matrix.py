import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(mat1.ndim, mat1.size, mat1.shape) # dimension 0 = row = axis
print(mat1.T)
v2 = np.array([1,2,3,4,5,6,7,8,9])
mat2 = v2.reshape(3,3)
print(mat2)
v3 = np.arange(12)
mat3 = v3.reshape(4,-1)
print(mat3)
v1 = mat1.reshape(-1)
print(v1)
# mat1.resize((4,), False)

print(mat2)
print(mat2[1:]) # filter row
print(mat2[1:, :-1]) # filter row + column
print(mat2[2,1])
print(mat2[:, 1])
print(mat2[:, 1:2])
print(mat2[mat2 < 5])

print(mat2.sum())
print(mat2.sum(axis=0))
print(mat2.sum(axis=1))

cube = np.array([1,2,3,4,5,6,7,8]).reshape(2,2,2)
print(cube)
print(cube.sum(axis=2))
cube333 = np.arange(27).reshape(3,3,3)
print(cube333.shape)
