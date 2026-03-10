# Créer le tableau x de -5 à +5 avec un pas de 0.1
# Afficher dans des subplots tanh la la sigmoide 1 / (1 + exp(-x))
# Dans tp_house afficher un nuage de point surfaces / loyers en déduire un modèle "apparent"
# Ne garder que les surfaces < 200m² et reafficher un nuage de points

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5,0.1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(x, np.tanh(x))
plt.subplot(2,1,2)
plt.plot(x, sigmoid(x))

data = np.load("data/house/house.npz")
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]

filter = surfaces < 175
surfaces175 = surfaces[filter]
loyers175 = loyers[filter]

plt.figure(2)
plt.subplot(2,1,1)
plt.scatter(surfaces, loyers)
plt.subplot(2,1,2)
plt.scatter(surfaces175, loyers175)
plt.show()