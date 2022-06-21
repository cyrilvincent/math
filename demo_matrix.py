import numpy as np


mat22 = np.array([[1,2,3], [4,5,6]])
print(mat22)
print(mat22.shape)

v1 = np.array([1,2,3,4,5,6])
print(v1.shape)
mat22 = v1.reshape(-1, 3)
print(mat22)
print(mat22.shape)