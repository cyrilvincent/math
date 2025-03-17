import numpy as np

data = np.load("data/house/house.npz")
print(data)

loyers = data["np_loyers"]
surfaces = data["np_surfaces"]
print(loyers)
print(surfaces)

print(loyers.size, surfaces.size)

# Créer le vecteur loyer_per_m2
# Pour chacun des 3 vecteurs, afficher min, max, sum/size
# Afficher le nombre de surface > 200
# Filtrer loyer ET surfaces par rapport à surface < 200