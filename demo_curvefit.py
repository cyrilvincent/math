import numpy as np
import random
import scipy.optimize as opt
import matplotlib.pyplot as plt

np.random.seed(0)
noise = 0.1
def f(x):
    """ function to approximate by polynomial interpolation"""
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    # f(x) = 2.5x.sin(0.7x)+2
    return  2.5 * x * np.sin(0.7 * x) + 2 + delta

x_plot = x = np.linspace(0, 10, 100)
np.random.shuffle(x)
x = np.sort(x[:20])
y = f(x)
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

plt.scatter(x_plot, f(x_plot))


# f(x) = ax.sin(bx)+c
# f = lambda x, a, b, c: a * x * np.sin(x * b) + c
p = lambda x, a, b, c, d: a * x ** 3 + b * x ** 2 + c * x + d

print(x.shape)
print(y.shape)
weigths, conv = opt.curve_fit(p, x, y)
print(weigths)
print(conv)

x = np.linspace(0, 10, 100)
plt.plot(x, p(x, weigths[0] , weigths[1], weigths[2], weigths[3]))
plt.show()