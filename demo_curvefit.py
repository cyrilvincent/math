import numpy as np
import random
import scipy.optimize as opt
import matplotlib.pyplot as plt

noise = 5
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

plt.scatter(x_plot, f(x_plot))
# plt.show()

# f(x) = ax.sin(bx)+c
g = lambda x, a, b, c: a * x * np.sin(x * b) + c


print(x.shape)
print(y.shape)
weigths, conv = opt.curve_fit(g, x, y)
print(weigths)
print(conv)