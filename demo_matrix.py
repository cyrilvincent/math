import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)
m2 = np.ones((2,2))
print(m2)
print(np.sin(m1 + m2))
print(m1.dot(m2))
print(np.dot(m1, m2))

m3 = np.array([[1,2,3],[4,5,6]])
print(m3)
print(m3.ndim, m3.size, m3.shape)
# print(m1 + m3)

# Reshape
v1 = np.arange(12)
m4 = v1.reshape(3,4)
print(m4)
m4 = v1.reshape(-1,3)
print(m4)
c1 = v1.reshape(2,3,2)
print(c1, c1.shape)
print(m4.reshape(-1))

print(v1, v1.shape)
print(v1.reshape(-1,1), v1.reshape(-1,1).shape)
print(v1.reshape(1,-1), v1.reshape(1,-1).shape)

m5 = np.array([2,4,6,8]).reshape(2,2)
print(m5)
res = np.linalg.inv(m5)
print(res)