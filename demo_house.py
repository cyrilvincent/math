import csv
import matplotlib.pyplot as plt
import numpy as np
import house_module as house
import house_oo

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    surfaces = [] # np.array([])
    loyers = []
    total = 0
    for row in reader:
        surface = float(row["surface"])
        # np.append(surfaces, surface)
        surfaces.append(surface)
        loyer = float(row["loyer"])
        loyers.append(loyer)
        loyer_m2 = loyer / surface
        total += loyer_m2
        print(surface, loyer, loyer_m2)
np_surfaces = np.array(surfaces)
np_loyers = np.array(loyers)
np_loyers_m2 = np_loyers / np_surfaces
print(f"Min: {np.min(np_loyers_m2)}, max: {np.max(np_loyers_m2)}")
print(np_loyers_m2[2:-2:3])
print(f"Shape: {np_surfaces.shape}")
loyer_m2_avg = total / len(surfaces)

# Surfaces < 200
# Intention
res = [x for x in surfaces if x <= 200]
# Filter
res = list(filter(lambda x: x <= 200, surfaces))
# NP

filter = np_surfaces < 200
surfaces_filter = np_surfaces[filter]
loyers_filter = np_loyers[filter]
print(surfaces_filter, loyers_filter)


# Afficher le nuage de point surface par loyer
# Calculer le loyer / m2 moyen
# Ecrire la lambda loyer_m2 * x
# Afficher le résulat de la fonction affine loyer_m2 en superposition

print(f"Loyer m2 moyen: {loyer_m2_avg}")

f = lambda x: loyer_m2_avg * x

f_result = [f(x) for x in range(400)]

# Save results
np.savez("data/house/house.npz", np_surfaces = np_surfaces, np_loyers = np_loyers, np_loyers_m2 = np_loyers_m2)
np_loyers = None
dico = np.load("data/house/house.npz")
print(list(dico.keys()))
np_loyers = dico["np_loyers"]

loyers, surface = house.load_house("data/house/house.csv")

house_service = house_oo.HouseService()
house_service.load_house("data/house/house.csv")

plt.scatter(surfaces, loyers)
plt.plot(range(400), f_result, color="red")
plt.show()
