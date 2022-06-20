import csv
import matplotlib.pyplot as plt
import numpy as np

def predict_loyer(surface):
    avg = 37.66
    return surface * avg



with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyer = float(row["loyer"])
        loyers.append(loyer)
        surfaces.append(float(row["surface"]))

    loyers = np.array(loyers)
    surfaces = np.array(surfaces)

    print(np.min(loyers), np.max(loyers), np.mean(loyers))
    print(np.min(surfaces), np.max(surfaces), np.mean(surfaces))

    loyers_per_m2 = loyers / surfaces
    print(np.min(loyers_per_m2), np.max(loyers_per_m2), np.mean(loyers_per_m2))

    print(np.round(predict_loyer(100), 2))

    # f(x) = 37.66 * x
    f = lambda x: 37.66 * x
    y = predict_loyer(loyers)
    print(y)

plt.scatter(surfaces, loyers)
plt.show()



# Afficher le nuage de points x: surfaces, y: loyers
# Afficher le loyer min, max, mean et idem pour surface
# Créer le tableau loyer_per_m2 et afficher min, max, mean
# Créer la fonction predict_loyer(surface: float) -> float