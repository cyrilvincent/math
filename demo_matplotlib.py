import matplotlib
import matplotlib.pyplot as plt
import math

print(matplotlib.__version__)

x = range(100)

plt.subplot(211)
y = [math.sin(value / 20) for value in x]
plt.plot(x, y)

plt.subplot(212)
y = [math.cos(value / 20) for value in x]
plt.scatter(x, y)
plt.savefig("fig.png")
plt.show()