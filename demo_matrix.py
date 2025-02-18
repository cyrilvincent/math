import numpy as np

m22 = np.array([[1,2],[3,4]])
print(m22)
print(m22 * 4)
m23 = np.array([[1,2,3],[4,5,6]])
print(m23)
# print(m22 + m23)
print(np.sum(np.sin(m23)))
print(m23.size, m23.ndim, m23.shape)

v12 = np.arange(12)
m34 = v12.reshape(3,-1)
print(m34)
m43 = v12.reshape(-1,3)
print(m43)
c232 = v12.reshape(2,3,2)
print(c232)
v12 = m34.reshape(12)

print(m22)
print(np.sum(m22))
print(np.sum(m22, axis=0))
print(np.sum(m22, axis=1))