import numpy as np

np.random.seed(0)
v1 = np.arange(0,10,0.1)
print(v1)
v2 = np.linspace(0,10,101)
print(v2)
v3 = np.random.random(10)
print(v3)
v4 = np.random.randint(0,5,10)
print(v4)
my_filter = v4 > 2.5
print(v4[my_filter])

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])
res = a1*a2
print(res)
print(np.sum(a1))
a3 = np.array([1,2,3])
# print(a1 + a3)
print(a1.ndim, a1.size, a1.shape, a1.dtype)

a4 = np.arange(1000)
print(a4[2:-2:2])
