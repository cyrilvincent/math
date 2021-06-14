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



# Afficher le min max moyenne : surfaces et des loyers
# loyer_per_m2 par une liste en intention
# Afficher le min max moyenne de loyer_per_m2, soit a = moyenne du moyer_per_m2
# Bonus afficher la courbe f(x) = ax
print(f"Loyers min {min(loyers):.2f}")
print(f"Loyers max {max(loyers):.2f}")
print(f"Loyers moy {sum(loyers) / len(loyers):.2f}")
print(f"Surfaces min {min(surfaces):.2f}")
print(f"Surfaces max {max(surfaces):.2f}")
print(f"Surfaces moy {sum(surfaces) / len(loyers):.2f}")
loyer_per_m2 = [l / s for l, s in zip(loyers, surfaces)]
print(loyer_per_m2)
print(f"Loyer par m² min {min(loyer_per_m2):.2f}")
print(f"Loyer par m² max {max(loyer_per_m2):.2f}")
print(f"Loyer par m² moy {sum(loyer_per_m2) / len(loyer_per_m2):.2f}")
plt.scatter(surfaces, loyers)
estimate_loyers = [37.66 * x for x in surfaces]
plt.plot(surfaces, estimate_loyers, color='red')
plt.show()