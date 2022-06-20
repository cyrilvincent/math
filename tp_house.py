import csv
import matplotlib.pyplot as plt

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyer = float(row["loyer"])
        loyers.append(loyer)
        surfaces.append(float(row["surface"]))

print(surfaces)
print(loyers)

plt.scatter(surfaces, loyers)
plt.show()

# Afficher le nuage de points x: surfaces, y: loyers
# Afficher le loyer min, max, mean et idem pour surface
# Créer le tableau loyer_per_m2 et afficher min, max, mean
# Créer la fonction predict_loyer(surface: float) -> loyer