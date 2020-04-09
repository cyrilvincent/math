import numpy as np
import matplotlib.pyplot as plt

l1 = [1,2,9,8,7,-2,3.14,-99,99,50]
v1 = np.array(l1)
v2 = np.arange(0,10)
v3 = np.random.rand(10)
print(v1, v2, v3)
v4 = v1 + v2
print(v4)
print(np.sin(v3 ** 2 + v1))
print(np.sin(np.pi))
print(np.sum(v2))
print(v2.shape)
print(v1[1],v1[-2])
print(v1[::2])

x = np.arange(-100,100)
mu = 0
sigma = 20

f = lambda x : 1/(np.sqrt(2*np.pi*np.power(sigma,2))) * np.exp(-np.power((x-mu),2)/(2*np.power(sigma,2)))

y = f(x)

plt.plot(x,y)
plt.show()

# sigmoide
# tanh


