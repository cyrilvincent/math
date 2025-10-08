import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as integrate

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
y += (np.random.rand(100) - 0.5) * 20

def f(x, a, b, c):
    return a * x ** 2 + b * x + c

def diff(x, a, b, c):
    return np.abs(f(x, a, b, c) - (2 * x ** 2 - x + 1))


array = opt.curve_fit(f, x, y)
print(array)

y2 = f(x,array[0][0],array[0][1],array[0][2])
plt.subplot(311)
plt.scatter(x, y)
plt.subplot(312)
plt.plot(x, y2, color="red")
plt.plot(x, 2*x**2-x+1, color="green")


y3 = diff(x,array[0][0],array[0][1],array[0][2])

result = integrate.quad(diff,0,2,args=(array[0][0],array[0][1],array[0][2]))
print(result)
plt.subplot(313)
print(x)
plt.plot(x, y3)
plt.show()
