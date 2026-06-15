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
# Créer le veceur loyer_inf_25 dont la surface est < 25
# Afficher la moyenne des loyers < 25