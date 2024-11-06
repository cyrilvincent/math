# data/house/house.npz
# keys = np_loyers, np_surfaces
# shape, min, max des loyers & surfaces
# loyers_m2 = np_loyers / np_surfaces -> min, max
# Filtrer les surfaces > 200 + compter (len)
# surfaces_filtered = surfaces < 200, afficher la shape
# loyers_filtered = surfaces < 200

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

data = np.load("data/house/house.npz")
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue, pvalue, stderr)
x = np.arange(400)
y = slope * x + intercept


plt.scatter(surfaces, loyers)
plt.plot(x, y, color="red")
plt.show()

# print(np.min(loyers), np.max(loyers), loyers.shape)
# print(np.min(surfaces), np.max(surfaces), surfaces.shape)
#
# loyers_m2 = loyers / surfaces
# print(loyers_m2)
# max = np.max(loyers_m2)
# print(loyers_m2[loyers_m2 == max], loyers[loyers_m2 == max], surfaces[loyers_m2 == max])
#
# surfaces200 = surfaces[surfaces >= 200]
# print(len(surfaces200))
#
surfaces_filtered = surfaces[surfaces < 200]
loyers_filtered = loyers[surfaces < 200]
slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_filtered, loyers_filtered)
print(slope, intercept, rvalue, pvalue, stderr)
x = np.arange(200)
y = slope * x + intercept
plt.scatter(surfaces_filtered, loyers_filtered)
plt.plot(x, y, color="red")
plt.show()