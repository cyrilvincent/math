import numpy as np

data = np.load("data/house/house.npz")
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]
print(loyers.dtype, loyers.size)
print(loyers)
print(surfaces)

# Afficher les min, max, sum/len des loyers et surfaces
# Créer le vecteur loyer_m2
# Afficher les surfaces > 200m²
# Afficher les loyers dont la surface > 200m²
# [(surface > 100) & (loyer < 1000)] & = AND, | OR, ! NOT tester surface > 100 ET loyer < 1000
