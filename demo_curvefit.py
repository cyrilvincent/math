import numpy as np
import random

noise = 0.01
def f(x):
    """ function to approximate by polynomial interpolation"""
    delta = (random.random() - 0.5) * noise
    # f(x) = 2.5 * x.sin(0.7x) + 2
    return  (2.5 + delta) * x * np.sin(x * (0.7 + delta)) + 2 + delta

x_plot = np.linspace(0, 10, 100)
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = np.sort(x[:20])
y = f(x)
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

# TP
# Fiter un polynome
# Refaire tp_house avec un polynome 

# f(x) = ax.sin(bx)+c
g = lambda x, a, b, c: a * x * np.sin(b * x) + c

def g(x, a, b, c):
    return a * x * np.sin(b * x) + c

import scipy.optimize as opt
print(x.shape)
print(y.shape)
weigths, conv = opt.curve_fit(g, x, y)
print(weigths)
print(conv)

import matplotlib.pyplot as plt
plt.scatter(x_plot, f(x_plot))
x = np.linspace(0, 10, 100)
y = g(x, weigths[0], weigths[1], weigths[2])
plt.plot(x, y, color="red")
plt.show()