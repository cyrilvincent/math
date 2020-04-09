#data = np.load("data/mesures/mesures.npz")
#mesures = data["mesures"]
#Faire le max et le min de la colonne 2 (Volt théorique) et 4 (Volt mesuré)
#|VT - VM| > bruit, bruit = 1v
#(VT - VM)² > bruit

import numpy as np
import matplotlib.pyplot as plt
data = np.load("data/mesures/mesures.npz")
mesures = data["mesures"]
print(mesures[:,2])
#plt.plot(mesures[:,2])
#plt.show()
