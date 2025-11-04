import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/house/house.npz")
print(data)
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]
print(surfaces)

# Afficher le nuage de points surfaces, loyers
# Afficher en console le min, max, sum des loyers
# Créer le tableau loyer_m2

plt.scatter(surfaces, loyers)
plt.show()

print(np.min(loyers), np.max(loyers))
loyer_m2 = loyers / surfaces
print(np.min(loyer_m2), loyer_m2.max())