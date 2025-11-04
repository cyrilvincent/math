import numpy as np
import matplotlib.pyplot as plt

l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(l1+l2)

a1 = np.array([1,2,3,4], dtype=np.int8)
a2 = np.array([5,6,7,8], dtype=np.int8)
print(a1 + a2)
print(a1.dtype)

a3 = np.arange(10,20,2)
print(a3)

rnd1 = np.random.rand(10)
print(rnd1)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.sin(x)
y2 = np.tanh(x)
plt.plot(x,y)
plt.show()
plt.scatter(x, y2, color="red")
plt.show()