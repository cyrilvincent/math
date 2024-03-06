import numpy as np

a1 = np.arange(0,100,2)
print(a1)
a2 = np.linspace(0,100,49)
print(a2)
np.random.seed(0)
a3 = np.random.rand(10)
a4 = np.random.randint(0,100,10)
print(a4)
a5 = np.array([1,2,3,4])
a6 = np.array([5,6,7,8])
a7 = a5 + a6
print(a7)
a5 = a5 * 10
print(np.sin(a5))
print(np.max(a5))

# print(a3 + a5)
print(a5.shape, a5.ndim, a5.size, a5.dtype)

print(a5[::-1])

print(a6 % 2 == 0)
my_filter = a6 % 2 == 0
print(a6[my_filter])
print(a6[a6 % 2 == 0])