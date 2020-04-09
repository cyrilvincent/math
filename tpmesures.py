#data = np.load("data/mesures/mesures.npz")
#mesures = data["mesures"]
#Faire le max et le min de la colonne 2 (Volt théorique) et 4 (Volt mesuré)
#|VT - VM| > bruit, bruit = 1v
#(VT - VM)² > bruit

import numpy as np
import matplotlib.pyplot as plt
data = np.load("data/mesures/mesures.npz")
mesures = data["mesures"]
plt.plot(mesures[:,4])

noise = 1
res1 = mesures[np.abs(mesures[:,2] - mesures[:,4]) > 1]
plt.scatter(res1[:,0], res1[:,4])
plt.show()

res2 = mesures[np.power(mesures[:,2] - mesures[:,4], 2) > 1]
