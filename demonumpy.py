import numpy as np
import matplotlib.pyplot as plt

l1 = [1,2,3,9,50,-2,3.14,6.66]
a1 = np.array(l1)
print(a1.dtype)
a2 = np.arange(8)
print(a2)
a3 = np.random.rand(8)
print(a3)
print(a1 ** 2)
print(np.sin(np.pi))
print(np.sin(a2))
print(a2.shape)
print(a2.ndim)
print(a2[:])

np.random.seed(0)
x = np.random.rand(10)
print(x)
print(x > 0.5)
print(x[x > 0.5])

finc = lambda x : x + 1
print(finc(x[x > 0.5]))

x = np.arange(-10,10,0.01)
sigmoidFn = lambda x : 1 / (1 + np.exp(-x))
y = sigmoidFn(x)
np.savez("data.npz",x = x, y = y)
x = None
y = None
data = np.load("data.npz")
x = data["x"]
y = data["y"]
plt.plot(x,y)
plt.show()

# TP
# Reprendre le COVID
# Créer 2 np.array : nbcas et dc
# Filtrer nbcas > 10
# Créer un np.array letalite = dc / nbcas
# Chercher le nbcas max, dc max, letalite max


