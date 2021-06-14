import matplotlib
import matplotlib.pyplot as plt
import math
import csv

print(matplotlib.__version__)

x = range(100)
y = range(100)
y2 = [math.sin(x / 20) for x in y]
y3 = [math.cos(x / 30) for x in y]

# plt.subplot(221)
# plt.plot(x, y2)
# plt.subplot(222)
# plt.plot(x, y3)
# plt.savefig("fig.png")
# plt.show()

loyers = []
surfaces = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))
print(loyers)

plt.scatter(surfaces, loyers)
plt.show()

# Afficher le min max moyenne : surfaces et des loyers
# loyer_per_m2 par une liste en intention
# Afficher le min max moyenne de loyer_per_m2, soit a = moyenne du moyer_per_m2
# Bonus afficher la courbe f(x) = ax
res = [(l, s) for l, s in zip(loyers, surfaces)]
