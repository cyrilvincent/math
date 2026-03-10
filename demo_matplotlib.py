import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi,0.1)
y = np.sin(x)
y2 = np.cos(x)

# plt.subplot(2,2,1)
plt.figure(1)
plt.title("sin x")
plt.plot(x, y, label="sin")
plt.plot(x, y2, color="red", label="cos")
plt.legend()

# plt.subplot(2,2,4)
plt.figure(2)
plt.scatter(x, y, label="sin")
plt.legend()
plt.show()
