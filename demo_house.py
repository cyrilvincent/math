import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt

data = np.load("data/house/house.npz")
print(data)
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]

print(loyers, np.min(loyers), np.max(loyers))

loyers_per_m2 = loyers / surfaces
print(np.min(loyers_per_m2), np.max(loyers_per_m2), np.mean(loyers_per_m2))

loyers_predicted = 30.66 * surfaces

mse = np.mean((loyers_predicted - loyers) ** 2)
print(np.sqrt(mse))

max = 200
predicat = surfaces < max
print(predicat)
loyers_filtered = loyers[predicat]
surfaces_filtered = surfaces[predicat]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_filtered, loyers_filtered)
print(slope, intercept, rvalue, pvalue, stderr)

x = np.arange(200)
y = slope * x + intercept

def poly2(x,a,b,c):
    return a * x ** 2 + b * x + c

weight2, conv2 = opt.curve_fit(poly2, surfaces, loyers)

plt.scatter(surfaces_filtered, loyers_filtered)
plt.plot(x, y, color="red")
plt.plot(x, poly2(x, weight2[0], weight2[1], weight2[2]), color="green")
plt.show()




