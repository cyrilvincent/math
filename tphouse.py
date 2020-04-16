import csv
import numpy as np

with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
loyers = np.array([float(x["loyer"]) for x in reader])
print(loyers)
surfaces = np.array([float(x["surface"]) for x in reader])
print(surfaces)

import matplotlib.pyplot as plt



# Afficher la moyenne des loyers et la mediane, en deduire s'il faut afficher l'ecart type ou un quantile
# Afficher la moyenne des surfaces et la mediane, en deduire s'il faut afficher l'ecart type ou un quantile
# Afficher les loyers/m², moyenne, mediane, ecart type
# Filtrer les points > 3 ecart types

print(np.mean(loyers), np.median(loyers), np.std(loyers))
print(np.mean(surfaces), np.median(surfaces), np.std(surfaces))
loyerm2 = loyers / surfaces
print(loyerm2)
print(np.mean(loyerm2), np.median(loyerm2), np.std(loyerm2))
std = np.std(loyerm2)
print(len(loyerm2))
loyerm2 = loyerm2[np.abs(loyerm2 - 37.66) < 3 * std]
print(len(loyerm2))

import scipy.stats as stats
slope, intercept, r_value, p_value,std_err = stats.linregress(surfaces, loyers)
print(slope, intercept, r_value, p_value,std_err)
# f(x) = 41x - 283

# Rejouer tphouse
# Filtrer les loyers > 3 * std et recalculer la regression linéaire avec curvefit
# f(x) = ax2 + bx + c
# f(x) = ax3 + bx2 + cx + d

filter = np.abs((41 * surfaces - 283) - loyers) < 3 * np.std(loyers)
loyers = loyers[filter]
surfaces = surfaces[filter]

plt.scatter(surfaces, loyers)

import scipy.optimize as opt
f1 = lambda x,a,b : a*x + b
f2 = lambda x,a,b,c : a*x**2 + b*x + c
f3 = lambda x,a,b,c,d : a*x**3 + b*x**2 + c*x + d
weigths, conv = opt.curve_fit(f1,surfaces,loyers)
print(weigths, conv)
weigths, conv = opt.curve_fit(f2,surfaces,loyers)
print(weigths, conv)
weigths, conv = opt.curve_fit(f3,surfaces,loyers)
print(weigths, conv)

plt.plot(np.arange(400), f3(np.arange(400),weigths[0],weigths[1],weigths[2],weigths[3]))
plt.show()




