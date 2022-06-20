# install matplotlib
import matplotlib.pyplot as plt
import math

x = [0.1,0.2,0.5,0.6,0.7,0.8,0.9]
y = range(7)

def sin(l):
    res = []
    for i in l:
        res.append(math.sin(i))
    return res

plt.scatter(x, y)
plt.show()
plt.plot(x, sin(x))
plt.show()



