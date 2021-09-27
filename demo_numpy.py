import numpy as np
v1 = np.array([1,2])
v2 = np.array([3,4])
print(v1 * v2)
print(np.dot(v1, v2))
print(v1.dot(v2))
print(np.sum(v1))

t1 = np.random.rand(10) * 5
#print(t1.astype("int32"))
t2 = np.random.randint(5,size=10)
print(t1+t2)
print(t1.shape, t1.ndim, t1.size, t1.dtype)

