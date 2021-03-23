import csv
import matplotlib.pyplot as plt

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))

plt.scatter(surfaces, loyers)
plt.show()

# TP
# Convertir en np.array
# loyers : min, max, moyenne, std, median, quantile
# surfaces : min, max, moyenne, std, median, quantile
# loyers_par_m² : créer le np.array : min, max, moyenne, std, median, quantile
# Déduire si c'est gaussien, afficher la distribution des loyers par m2, afficher plot(loyers_par_m2)
# Enlever les points > 150m²
# recalculer le tout => Conclusion