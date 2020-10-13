import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.stats as stats

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))
    loyers = np.array(loyers)
    surfaces = np.array(surfaces)
    print(loyers.shape)
    print(surfaces.shape)

plt.scatter(surfaces, loyers)

print(np.min(loyers), np.max(loyers), np.mean(loyers), np.median(loyers), np.std(loyers), np.quantile(loyers, [0.25]))

loyerperm2 = loyers / surfaces

print(np.min(loyerperm2), np.max(loyerperm2), np.mean(loyerperm2), np.median(loyerperm2), np.std(loyerperm2), np.quantile(loyerperm2, [0.25]))

coef, intercept, rvalue,pvalue,stderr = stats.linregress(surfaces, loyers)
print(coef, intercept, rvalue,pvalue,stderr)

f = lambda x : coef * x + intercept
x = np.arange(0,400)
plt.plot(x, f(x),color="red")

std = np.std(loyerperm2) # 9.64

surfaces_filtre = surfaces[surfaces < 200]
loyers_filtre = loyers[surfaces < 200]

filtre = np.abs(f(surfaces_filtre) - loyers_filtre) < 3 * std * surfaces_filtre
surfaces_filtre = surfaces_filtre[filtre]
loyers_filtre = loyers_filtre[filtre]

coef, intercept, rvalue,pvalue,stderr = stats.linregress(surfaces_filtre, loyers_filtre)
print(coef, intercept, rvalue,pvalue,stderr)

x = np.arange(0,200)
plt.plot(x, coef * x + intercept,color="green")

plt.show()

