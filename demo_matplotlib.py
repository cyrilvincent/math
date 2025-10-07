import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(100)
# y = np.arange(100)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.title("Trigo")
# plt.subplot(221)
plt.scatter(x, y, label="sin")
# plt.subplot(224)
plt.plot(x, y2, color="red", label="cos",)
plt.legend()
plt.savefig("figure.png")
plt.show()