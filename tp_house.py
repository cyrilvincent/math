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

print(np.min(loyers), np.max(loyers), np.sum(loyers)/len(loyers))
print(np.min(surfaces), np.max(surfaces), np.sum(surfaces)/len(surfaces))
loyer_m2 = loyers / surfaces
print(loyer_m2)
print(surfaces[surfaces > 200])
print(loyers[surfaces > 200])
filter = surfaces > 200
print(loyers[filter])
filter2 = (surfaces > 100) & (loyers < 2500)
print(loyers[filter2])
print(surfaces[filter2])

import pickle
with open("data/house/house.pkl", "wb") as f:
    pickle.dump(loyers, f)

with open("data/house/house.pkl", "rb") as f:
    loyers = pickle.load(f)