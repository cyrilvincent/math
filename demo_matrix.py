import numpy as np

m1 = np.array([[1,2],[3,4]]) # Row first
print(m1)
m2 = np.array([[1,2,3],[4,5,6]])
print(m2, m2.shape)
print(m2.T, m2.T.shape)
v3 = np.array([1,2,3])
print(v3, v3.shape)
m3 = np.array([[1,2,3]])
print(m3, m3.shape)
print(m3.T, m3.T.shape)

m4 = np.array([[5,6],[7,8]])
print(m1+m4)
print(m1*m4)
# print(m1 * m2)
print(np.sin(m1))
print(m2**2 * 3)

# print(m2 * m2.T)
v12 = np.arange(1, 13)
print(v12, v12.shape, v12.ndim, v12.size)
m34 = v12.reshape(-1,4)
print(m34, m34.shape, m34.ndim, m34.size)
m43 = v12.reshape(4,-1)
print(m43, m43.shape, m43.ndim, m43.size)
v12bis = m34.reshape(12)
print(v12bis)
m121 = v12.reshape(1,12)
print(m121)
m121 = v12.reshape(12,1)
print(m121)
cube = v12.reshape(12,1,1)
print(cube, cube.shape)

print(m1)
print(np.linalg.inv(m1))

print(m1.dot(m4))
print(np.dot(m1,m4))

# Axis
print(m34)
print(np.sum(m34))
print(np.sum(m34, axis=0)) #ndim -= 1
print(np.sum(m34, axis=1)) #ndim -= 1
print(m43[1:-1])
