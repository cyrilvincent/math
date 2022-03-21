import csv
import matplotlib.pyplot as plt

import numpy as np

surfaces = []
loyers = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))
surfaces = np.array(surfaces)
loyers = np.array(loyers)
print(loyers)
print(surfaces)

# Afficher le loyer max, la surface max
# Créer le tableau loyer/m², display, min, max, mean
# Essayer d'afficher la fonction linéaire y = mean*x

plt.scatter(surfaces, loyers)
plt.show()
