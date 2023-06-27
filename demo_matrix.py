import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
mat_rnd = np.random.rand(4,3)
print(mat_rnd * 10)

mat2 = np.array([[5,6],[7,8]])
mat3 = np.array([[1,2,3],[4,5,6]])
print(mat1 + mat2)
# print(mat1 + mat3)
print(mat3.shape, mat3.ndim, mat3.size)

print(mat1 * 2)
print(mat1 ** 2)
print(np.sin(mat1))

v1 = np.array([2,3])
print(mat1 * v1)

mat3 = np.array([[1,2,3],[4,5,6]])
print(mat3.shape)
print(mat3.reshape(3,2))
print(mat3.reshape(6))
v1 = np.arange(6)
print(v1.reshape(2,3))
print(mat3.reshape(3,2,1))
print(mat3.reshape(-1,3))
print(mat3.T)

mat4 = np.array([[2,4], [6,8]])
print(np.linalg.matrix_rank(mat4))
print(np.trace(mat4))
print(np.linalg.inv(mat4))

# mat4 = np.array([[2,4], [4,8]])
# print(np.linalg.matrix_rank(mat4))
# print(np.trace(mat4))
# print(np.linalg.inv(mat4))

mat4 = np.array([[1,2], [3,4]])
print(np.linalg.matrix_rank(mat4))
print(np.trace(mat4))
print(np.linalg.inv(mat4))

print(mat1.sum())
print(mat1.sum(axis=0))
print(mat1.sum(axis=1))

cube = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
print(cube.shape)
print(cube)
print(cube[0])
print(cube[:,0])
print(cube[:,:,0])
print(cube.sum())
print(cube.sum(axis=2))