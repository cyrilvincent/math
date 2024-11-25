import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x
y2 = x / 2
plt.subplot(121)
plt.plot(x, y, label="Courbe 1")
plt.subplot(122)
plt.bar(x, y2, label="Courbe 2")
plt.savefig("data/essai.png")
plt.legend()
plt.title("Mon superbe graphique")
plt.show()