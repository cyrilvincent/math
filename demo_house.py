import csv
import matplotlib.pyplot as plt

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    surfaces = []
    loyers = []
    total = 0
    for row in reader:
        surface = float(row["surface"])
        surfaces.append(surface)
        loyer = float(row["loyer"])
        loyers.append(loyer)
        loyer_m2 = loyer / surface
        total += loyer_m2
        print(surface, loyer, loyer_m2)
    loyer_m2_avg = total / len(surfaces)


# Afficher le nuage de point surface par loyer
# Calculer le loyer / m2 moyen
# Ecrire la lambda loyer_m2 * x
# Afficher le résulat de la fonction affine loyer_m2 en superposition

print(f"Loyer m2 moyen: {loyer_m2_avg}")

f = lambda x: loyer_m2_avg * x

f_result = [f(x) for x in range(400)]

plt.scatter(surfaces, loyers)
plt.plot(range(400), f_result, color="red")
plt.show()

