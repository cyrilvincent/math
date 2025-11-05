import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt
import sklearn.neighbors as n

n.KNeighborsClassifier(n)

data = np.load("data/house/house.npz")
print(data)
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]
print(surfaces)


opt.curve_fit()
# Afficher le nuage de points surfaces, loyers
# Afficher en console le min, max, sum des loyers
# Créer le tableau loyer_m2



print(np.min(loyers), np.max(loyers))
loyer_m2 = loyers / surfaces
print(np.min(loyer_m2), loyer_m2.max())

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue, pvalue, stderr)

x = np.arange(400)
y = slope * x + intercept

plt.scatter(surfaces, loyers)
plt.plot(x, y, color="red")
plt.show()


