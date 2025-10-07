import numpy as np

data = np.load("data/house/house.npz")
print(data)
loyers = data["np_loyers"]
surfaces = data["np_surfaces"]
print(loyers)
print(surfaces)

# Calculer loyer_per_m2
# Afficher les loyers, surfaces max et min
# Filtrer les surfaces < 200
# Filtrer les loyers dont la surface est > 200
# Filtrer les loyers dont la surface > 100 ET loyer < 2000
# Filtrer les loyers où surface > 200 OU loyer > 10000
# Sauvegarder un des resultats