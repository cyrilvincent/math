import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)
np.random.seed(42)
rnd22 = np.random.rand(2,2)
print(rnd22)
print(m1 * rnd22)
print(m1.dtype, m1.ndim, m1.size, m1.shape)
mat23 = np.array([[1,2],[3,4],[5,6]])

print(np.dot(m1, rnd22))
# print(mat23 + rnd22)
# Numpy = row first

v12 = np.arange(12)
mat34 = v12.reshape(3, 4)
print(mat34, mat34.shape)
mat43 = v12.reshape(4, 3).T
print(mat43)
mat26 = v12.reshape(2, -1)
mat62 = v12.reshape(-1, 2)

v12 = mat34.reshape(12)
print(v12)

cube232 = v12.reshape(2,3,2)
print(cube232)