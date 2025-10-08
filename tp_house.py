import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt

data = np.load("data/house/house.npz")
print(data)
loyers = data["np_loyers"]
surfaces = data["np_surfaces"]
print(loyers)
print(surfaces)

# Calculer loyer_per_m2
# Afficher les loyers, surfaces max et min
# Filtrer les surfaces < 200
# Filtrer les loyers dont la surface est > 200
# Filtrer les loyers dont la surface > 100 ET loyer < 2500
# Filtrer les loyers où surface > 200 OU loyer > 10000
# Sauvegarder un des resultats

loyer_per_m2 = loyers / surfaces
print(loyer_per_m2)
print(np.min(loyers), np.max(loyers))
surfaces_inf_200 = surfaces[surfaces < 200]
print(surfaces_inf_200)
print(loyers[surfaces > 200])
result = loyers[(loyers < 2500) & (surfaces > 100)]
print(result.size)
print(loyers[(surfaces > 200) | (loyers > 10000)])
np.savez("save.npz", result=result)

def f(x, a, b, c):
    return a * x ** 2 + b * x + c

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(rvalue, pvalue)
result = opt.curve_fit(f,surfaces, loyers)
print(result)
x = np.arange(400)
y = slope * x + intercept
y2 = f(x,result[0][0],result[0][1],result[0][2])
plt.scatter(surfaces, loyers)
plt.plot(x, y, color="red")
plt.plot(x, y2, color="maroon")
plt.show()