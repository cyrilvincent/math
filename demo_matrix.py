import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)

m23 = np.array([[1,2,3],[4,5,6]])
print(np.sin(m23) * 2)

print(m23.ndim, m23.size, m23.shape)

print(m23.T)

v6 = np.arange(6)
print(v6)
m16 = np.array([[1,2,3,4,5,6]])
print(m16)
m61 = m16.T
print(m61)

v12 = np.arange(12)
print(v12)
m34 = v12.reshape(3,4)
print(m34)
m43 = v12.reshape(-1,3)
print(m43)
c232 = v12.reshape(2,3,-1)
print(c232)

print(m1)
print(np.sum(m1))
print(np.sum(m1, axis=0))
print(np.sum(m1, axis=1))