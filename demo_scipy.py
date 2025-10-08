import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# pip install scipy

x = np.arange(100)
y = 2. * x + 1
y += (np.random.rand(100) - 0.5) * 20

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
print(slope, intercept, rvalue, pvalue, stderr)
y2 = slope * x + intercept

# plt.scatter(x, y)
# plt.plot(x, y2, color="red")
# plt.show()

x = np.linspace(-10,10,100)
y = 2 * x **2 - x + 1
y += (np.random.rand(100) - 0.5) * 200

def f(x, a, b, c):
    return a * x ** 2 + b * x + c

array = opt.curve_fit(f, x, y)
print(array)

y2 = f(x,array[0][0],array[0][1],array[0][2])
plt.scatter(x, y)
plt.plot(x, y2, color="red")
plt.show()