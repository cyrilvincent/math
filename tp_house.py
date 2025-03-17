import numpy as np
import matplotlib.pyplot as plt

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

loyer_per_m2 = loyers / surfaces
print(loyer_per_m2)
print(np.min(loyers), np.max(loyers), np.mean(loyers))
print(np.min(surfaces), np.max(surfaces), np.mean(surfaces))
print(np.min(loyer_per_m2), np.max(loyer_per_m2), np.mean(loyer_per_m2))

surf200 = surfaces[surfaces > 200]
nb = surf200.size
print(nb)

predicate = surfaces < 200
surfaces_filtered = surfaces[predicate]
loyers_filtered = loyers[predicate]

print(surfaces_filtered)

# plt.subplot(211)
plt.scatter(surfaces, loyers, color="blue")
plt.show()

# Afficher le nuage de point surfaces / loyers
# Idem pour les surfaces et loyers filtrés