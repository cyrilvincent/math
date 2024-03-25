import matplotlib.pyplot as plt
import random

x = range(100)
y = range(100)

plt.subplot(221)
plt.plot(x, y, "rx-")

x = range(100)
y = []
for i in x:
    y.append(random.randint(0,10))

plt.subplot(222)
plt.scatter(x, y)

x = range(10)
y = []
for i in x:
    y.append(random.randint(0,10))
plt.subplot(223)
plt.bar(x, y, color="red")
plt.show()