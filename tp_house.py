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

plt.scatter(surfaces, loyers)
plt.show()
