import numpy as np

mat22 = np.array([[1,2],[3,4]])
print(np.cos(mat22))
mat23 = np.array([[1,2,3],[4,5,6]])
print(mat23)

print(mat22.ndim, mat22.size, mat22.shape)
print(mat23.ndim, mat23.size, mat23.shape)

v12 = np.arange(12)
print(v12)
mat34 = v12.reshape(3,-1)
print(mat34)
mat43 = v12.reshape(-1, 3)
print(mat43)
print(mat43.shape)
cube = v12.reshape(2,-1,2)
print(cube)
print(cube.reshape(12))