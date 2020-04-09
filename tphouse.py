import csv
import numpy as np

with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
loyers = np.array([float(x["loyer"]) for x in reader])
print(loyers)
surfaces = np.array([float(x["surface"]) for x in reader])
print(surfaces)

import matplotlib.pyplot as plt
plt.scatter(surfaces, loyers)
plt.show()

# Afficher la moyenne des loyers et la mediane, en deduire s'il faut afficher l'ecart type ou un quantile
# Afficher la moyenne des surfaces et la mediane, en deduire s'il faut afficher l'ecart type ou un quantile
# Afficher les loyers/m², moyenne, mediane, ecart type
# Filtrer les points > 3 ecart types