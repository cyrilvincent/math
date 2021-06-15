import matplotlib
import matplotlib.pyplot as plt
import math
import csv
import numpy as np



loyers = []
surfaces = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))

loyers_array = np.array(loyers)
surfaces_array = np.array(surfaces)
loyers_per_m2 = loyers_array / surfaces_array

print(np.min(loyers_per_m2), np.max(loyers_per_m2), np.mean(loyers_per_m2))

plt.scatter(surfaces_array, loyers_per_m2)
plt.show()

# Filtrers les data surface > 150
# Afficher la courbe x = surface, y = loyer
# Filtrer loyers_per_m2
# Recalculer le min, max, avg