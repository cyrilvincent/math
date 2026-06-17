import scipy.optimize as opt
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

x = np.arange(0, 10, 0.1)
factor = 1
noise = (np.random.rand(len(x)) - 0.5) * 2 * factor
def f(x):
    return 2.5 * x * np.sin(0.7 * x) + 2 + noise

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def poly3_abs(x, a, b, c, d):
    return np.abs(poly3(x, a, b, c, d))

def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

y = f(x)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)

weight, conv = opt.curve_fit(poly2, x, y)
print(weight)
print(conv)

weight3, conv3 = opt.curve_fit(poly3, x, y)
print(weight3)
print(conv3)

weight_sin, conv_sin = opt.curve_fit(xsinx, x, y)
print(weight_sin)
print(conv_sin)

area = integrate.quad(poly3_abs, 0, 5, args=(weight3[0], weight3[1], weight3[2], weight3[3]))
print(f"Area: {area}")

plt.plot(x, slope * x + intercept, color="red")
plt.plot(x, poly2(x, weight[0], weight[1], weight[2]), color="yellow")
plt.plot(x, poly3(x, weight3[0], weight3[1], weight3[2], weight3[3]), color="maroon")
plt.plot(x, xsinx(x, weight_sin[0], weight_sin[1], weight_sin[2]), color="black")
plt.scatter(x, y)
plt.show()



# Calculer la surface de 0 à 5 de poly3