import numpy as np
import math
import matplotlib.pyplot as plt

# def addlist(l1, l2):
#     res = []
#     if len(l1) == len(l2):
#         for ix, value in enumerate(l1):
#             res.append(l1[ix]+l2[ix])
#     return res

a1 = np.array([1,2,3], dtype=np.float64)
a2 = np.array([4,5,6])
a3 = np.arange(7,10)
res = a1 + a2 + a3
print(res)
print(np.sin(a1) + np.cos(a2))

res = list(map(lambda x : math.sin(x), a1))
print(res)

print(a1.ndim, len(a1), a1.shape)

a4 = np.array([1,2,5,8,9,10,12,20,50,4,2])
a5 = np.array([2,2,52,8,99,101,102,20,50,98,2])
print(a4[3])
print(a4[-1])
print(a4[2:8])
print(a4[:8])
print(a4[2:])
print(a4[:])
print(a4[2:8:2])
print(a4[::2])

print(a4 >= 10)
print(a4[[True, True, False, False, True, False, True, False, True, False, False]])
print(a4[a4 >= 10])
print(a5[a4 >= 10])

a1 = np.array([1,2,3,4])
a2 = np.ones(4)
print(a1 ** 2)
print(np.sin(a1) * 2)
print(a1[a1 < 3])

f = lambda x: x + 1
def f(x):
    return x+1
print(f(a1))

x = np.linspace(-10,10,1000)
fsigmoide = lambda x : 1 / (1 + np.exp(-x))
y = fsigmoide(x)
np.savez("data.npz", x=x, y=y)
x = None
y = None
data = np.load("data.npz")
x = data["x"]
y = data["y"]
plt.plot(x, y)
# plt.show()

v1 = np.array([1,2])
v2 = np.array([3,4])
print(v1 * v2)
print(v1.dot(v2))
m1 = np.array([[1,2],[3,4]])
print(m1)
# print(m1[0])
print(m1.shape)
print(np.sum(m1, axis=1))