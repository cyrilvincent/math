import csv
import matplotlib.pyplot as plt

loyers = []
surfaces = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyer = float(row["loyer"])
        loyers.append(loyer)
        surfaces.append(float(row["surface"]))
print(loyers)
print(surfaces)

# TP
# Afficher dans maptplotlib le nuage de points x = surfaces, y = loyers
# Rendre le diagramme "pretty"
# Calculer le loyer moyen, surface moyenne => sum()/len()

avg_loyer = sum(loyers) / len(loyers)
print(avg_loyer)
avg_surface = sum(surfaces) / len(surfaces)
print(avg_surface)
plt.scatter(surfaces, loyers)
plt.show()

# Convertir les listes python en tableau numpy
# np.mean
# Recalculer les moyennes
# Calculer la moyenne du loyer/m²
import numpy as np
loyers_np = np.array(loyers)
surfaces_np = np.array(surfaces)
print(np.min(loyers_np), np.max(loyers_np), np.mean(loyers_np))
print(np.min(surfaces_np), np.max(surfaces_np), np.mean(surfaces_np))
loyer_per_m2 = loyers_np / surfaces_np
print(np.min(loyer_per_m2), np.max(loyer_per_m2), np.mean(loyer_per_m2))

t1 = np.array([1,2,3,4,5,6.])
print(t1[[True,True,True,False,False,False]])
print(t1 < 4)
print(t1[t1 < 4])

# Filtrer les surfaces et loyers par rapport surface < 200
# Reafficher les data dans matplotlib
# Recalculer la moyenne
# Bonus : Afficher sur le même diagrame f(x) = ax où a = moyenne

filtre = surfaces_np < 200
surfaces_filtre = surfaces_np[filtre]
loyers_filtre = loyers_np[filtre]
loyers_per_m2_filtre = loyers_filtre / surfaces_filtre
print(np.mean(loyers_per_m2_filtre))
plt.scatter(surfaces_filtre, loyers_filtre)
plt.show()