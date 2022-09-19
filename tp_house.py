import numpy as np
import csv
import matplotlib.pyplot as plt

surf=[]
loyer=[]
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        surf.append(float(row["surface"]))
        loyer.append(float(row["loyer"]))

surf = np.array(surf)
loyer = np.array(loyer)

print(surf)
print(loyer)

# TP
# Afficher le shape de surf et loyer, sont il compatibles
# Afficher le nuage de point x = surf, y = loyer
# np.sum() len()
# Afficher le loyer moyen et la surface moyenne
# Créer le tableau loyer_par_m2
# Afficher le loyer par m² moyen
# Afficher en subplot le diagramme en barre des loyer par m²

print(surf.shape, loyer.shape)
plt.subplot(211)
plt.scatter(surf, loyer)
print(np.mean(surf), np.mean(loyer))
loyer_par_m2 = loyer / surf
print(loyer_par_m2)
plt.subplot(212)
plt.bar(surf, loyer_par_m2)
plt.show()

predicat = surf < 200
print(predicat)
surf2 = surf[predicat]
print(surf2)
loyer2 = loyer[predicat]

# group1 = 0 < surf <= 40
# group2 = 40 < surf <= 80
# group3 = surf > 80
#
# loyer1 = loyer[group1]
# loyer2 = loyer[group2]
# loyer3 = loyer[group3]
#
# surf1 = loyer[group1]
# surf2 = loyer[group2]
# surf3 = loyer[group3]
