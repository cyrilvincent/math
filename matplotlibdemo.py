import matplotlib.pyplot as plt
import math

x = list(range(100))
y1 = [math.cos(value / 15) for value in x]
y2 = [math.sin(value / 20) for value in x]
plt.legend("Demo")
plt.subplot(121) # [2,1,1]
plt.plot(x, y1, label="y1")
plt.subplot(122)
plt.plot(x, y2, label="y2")
plt.show()
# plt.savefig("figure.png")