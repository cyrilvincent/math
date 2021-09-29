import csv
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

loyers = []
surfaces = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyer = float(row["loyer"])
        loyers.append(loyer)
        surfaces.append(float(row["surface"]))
print(loyers)
print(surfaces)

# TP
# Afficher dans maptplotlib le nuage de points x = surfaces, y = loyers
# Rendre le diagramme "pretty"
# Calculer le loyer moyen, surface moyenne => sum()/len()

avg_loyer = sum(loyers) / len(loyers)
print(avg_loyer)
avg_surface = sum(surfaces) / len(surfaces)
print(avg_surface)



# Convertir les listes python en tableau numpy
# np.mean
# Recalculer les moyennes
# Calculer la moyenne du loyer/m²

loyers_np = np.array(loyers)
surfaces_np = np.array(surfaces)
print(np.min(loyers_np), np.max(loyers_np), np.mean(loyers_np))
print(np.min(surfaces_np), np.max(surfaces_np), np.mean(surfaces_np))
loyer_per_m2 = loyers_np / surfaces_np
print(np.min(loyer_per_m2), np.max(loyer_per_m2), np.mean(loyer_per_m2))

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_np, loyers_np)
print(slope, intercept, rvalue, pvalue, stderr)
faffine = lambda x : slope * x + intercept

plt.scatter(surfaces, loyers)
plt.plot(np.arange(400), faffine(np.arange(400)), color="green" )
plt.show()


# Filtrer les surfaces et loyers par rapport surface < 200
# Reafficher les data dans matplotlib
# Recalculer la moyenne
# Bonus : Afficher sur le même diagrame f(x) = ax où a = moyenne

filtre = surfaces_np < 200
surfaces_filtre = surfaces_np[filtre]
loyers_filtre = loyers_np[filtre]
loyers_per_m2_filtre = loyers_filtre / surfaces_filtre
moyenne = np.mean(loyers_per_m2_filtre)

flineaire = lambda x: moyenne * x
x = np.arange(200)
y = flineaire(x)
plt.plot(x, y, color="red")

plt.scatter(surfaces_filtre, loyers_filtre)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_filtre, loyers_filtre)
print(slope, intercept, rvalue, pvalue, stderr)

faffine = lambda x : slope * x + intercept
y2 = faffine(x)
plt.plot(x, y, color="green")
plt.show()

np.savez("data/house/house_filtre.npz", surfaces_filtre=surfaces_filtre, loyers_filtre=loyers_filtre)
data = np.load("data/house/house_filtre.npz")
surfaces_filtre_2 = data["surfaces_filtre"]
loyers_filtre_2 = data["loyers_filtre"]