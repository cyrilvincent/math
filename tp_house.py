import csv
import matplotlib.pyplot as plt
import mylib

import numpy as np

def f(x):
    return x + 1

surfaces = []
loyers = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))
surfaces = np.array(surfaces)
loyers = np.array(loyers)
# print(loyers)
# print(surfaces)

print(f"min: {np.min(loyers)}, max: {np.max(loyers)}, avg: {np.mean(loyers):.2f}")
print(f"min: {np.min(surfaces)}, max: {np.max(surfaces)}, avg: {np.mean(surfaces)}")

loyer_per_m2 = loyers / surfaces
print(f"min: {np.min(loyer_per_m2)}, max: {np.max(loyer_per_m2)}, avg: {np.mean(loyer_per_m2)}")
avg = np.mean(loyer_per_m2)
y = surfaces * avg

f = lambda x: avg * x
g = lambda x: x ** 2

# Afficher le loyer max, la surface max
# Créer le tableau loyer/m², display, min, max, mean
# Essayer d'afficher la fonction linéaire y = mean*x


mylib.display(surfaces, loyers, loyer_per_m2, fn=lambda x: avg * x)
