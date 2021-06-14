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
print(loyers_array)

print(loyers_array / surfaces_array)

# Recalculer min, max , mean