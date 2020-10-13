import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/mesures/mesures.npz")
mesures = data["mesures"]
print(mesures.shape)
plt.plot(mesures[:,4])
plt.show()