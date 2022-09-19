import numpy as np
import csv

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