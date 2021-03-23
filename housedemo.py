import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def min_max_avg_std_median_quartile(a):
    return np.min(a), np.max(a), np.mean(a), np.std(a), np.median(a), np.quantile(a, 0.25),  np.max(a) - np.quantile(a, 0.75)


with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))

loyers = np.array(loyers)
surfaces = np.array(surfaces)
loyersstat = min_max_avg_std_median_quartile(loyers)
print(loyersstat)
surfstat = min_max_avg_std_median_quartile(surfaces)
print(surfstat)
loyerparm2 = loyers / surfaces
loyerparm2stat = min_max_avg_std_median_quartile(loyerparm2)
print(loyerparm2stat)
filter = surfaces < 150
loyerparm2filter = loyerparm2[filter]
loyer_par_m2_filter_stat = min_max_avg_std_median_quartile(loyerparm2filter)
print(loyer_par_m2_filter_stat)

slope, intercept, rvalue, pvalue, err = scipy.stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue, pvalue, err)

faffine = lambda surface : slope * surface + intercept
floyer = lambda surface : 37.4 * surface

plt.scatter(surfaces, loyers)
plt.plot(np.arange(400), faffine(np.arange(400)), color="red")
plt.show()

# TP
# Convertir en np.array
# loyers : min, max, moyenne, std, median, quantile
# surfaces : min, max, moyenne, std, median, quantile
# loyers_par_m² : créer le np.array : min, max, moyenne, std, median, quantile
# Déduire si c'est gaussien, afficher la distribution des loyers par m2, afficher plot(loyers_par_m2)
# Enlever les points > 150m²
# recalculer le tout => Conclusion