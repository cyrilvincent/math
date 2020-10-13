import numpy as np

v1 = np.array([1,2,3,4,5,6,7,8])
m1 = v1.reshape(-1,2)
#print(m1)

m2 = np.array([[1,2],[3,4]])
m3 = np.array([[5,6],[7,8]])
m4 = m3 * m2
print(m4)

m5 = np.dot(m3, m2)
m5 = m2.dot(m3)
print(m5)

print(m2)
print(m2.sum(axis=-1))