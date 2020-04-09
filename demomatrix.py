import numpy as np
mat1 = np.array([[1,2],[3,4]])
print(mat1)

mat2 = np.random.rand(5,5) * 10
print(mat2)

mat3 = np.random.rand(2,2) * 10
print(mat3)

print(np.sin(mat1 + mat3) < 0)
print(mat3.shape)

print(np.linalg.inv(mat1))

v1 = np.array([1,2,3,4])
mat1 = v1.reshape(2,2)
print(mat1)
print(mat1.reshape(4))
print(mat1.T)

print(mat1.dot(mat3))
print(np.sum(mat1, axis=0))

# mat4 = np.random.rand(100)
# import matplotlib.pyplot as plt
#
# plt.scatter(np.arange(100), mat4)
# plt.show()

mat4 = np.random.rand(3,3) * 10
print(mat4)
print(mat4[mat4 < 5])


