import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
print(np.sin(mat1) * 2)
mat2 = np.array([[5,6],[7,8]])
print(mat2)
print(mat1 + mat2)

print(mat1.ndim, mat1.size, mat1.shape)

mat32 = np.array([[1,2], [3,4], [5,6]])
print(mat32)
print(mat32.ndim, mat32.size, mat32.shape)
print(mat32.T)

v12 = np.arange(12)
print(v12)
print(v12.shape)

mat34 = v12.reshape(3,4)
print(mat34)
mat43 = v12.reshape(4,-1)
print(mat43)
cube232 = v12.reshape(2,3,2)
print(cube232)
mat34.reshape(12)

res = np.linalg.inv(mat1)
print(res)

print(np.dot(mat1, mat2))

print(mat1)
print(np.sum(mat1))
print(np.sum(mat1, axis=1))

v150 = np.arange(150)
mat503 = v150.reshape(-1, 3)
print(mat503)

print(mat503[-10:10:-3,:])
