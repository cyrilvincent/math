import scipy.stats as stats
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

data = np.load("data/house/house.npz")
loyers = data["np_loyers"]
surfaces = data["np_surfaces"]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue, pvalue, stderr)



def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

factors, conv = opt.curve_fit(poly2, surfaces, loyers)
print(factors)
print(conv)

x = np.arange(400)
predicted = slope * x + intercept

res = integrate.quad(poly2, 11, 100, args=(factors[0], factors[1], factors[2]))
print(res)

plt.plot(x, predicted, color="red")
plt.plot(x, poly2(x, factors[0], factors[1], factors[2]), color="black")
plt.scatter(surfaces, loyers)
plt.show()
