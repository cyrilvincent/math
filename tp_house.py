import numpy as np

data = np.load("data/house/house.npz")
print(data)

loyers = data["np_loyers"]
surfaces = data["np_surfaces"]

print(loyers)

# Copier depuis le zip de github le répertoire data/* à la racine de votre projet
# Visualiser data/house/house.csv
# Charger le npz
# Afficher le shape des 2 vecteurs
# Afficher le min, max de chaque vecteur
# np.sum / .size
# Créer le vecteur loyer_m2
# Créer les vecteur surfaces_inf_25 qui concerne les surfaces < 25
# Créer le vecteur loyer_inf_25 dont la surface est < 25
# Afficher la moyenne des loyers < 25

print(loyers.shape, surfaces.shape)
print(loyers.min(), np.max(loyers), np.sum(loyers) / len(loyers))
print(surfaces.min(), np.max(surfaces), surfaces.sum() / loyers.size)

loyer_m2 = loyers / surfaces
print(loyer_m2.min(), np.max(loyer_m2), loyer_m2.sum() / loyer_m2.size)

filter = surfaces < 25
surfaces_inf_25 = surfaces[filter]
loyers_inf_25 = loyer_m2[filter]
print(loyers_inf_25.min(), np.max(loyers_inf_25), loyers_inf_25.sum() / loyers_inf_25.size)