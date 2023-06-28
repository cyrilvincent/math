import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

np.random.seed(0)
noise = 10
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    # f(x) = 2.5x.sin(0.7x)+2
    return  2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.linspace(0, 10, 100)
plt.scatter(x, f(x))


# f(x) = ax.sin(bx)+c
model = lambda x, a, b, c: a * x * np.sin(x * b) + c


weigths, conv = opt.curve_fit(model, x, f(x), bounds=([-np.inf, -np.inf, 2], [np.inf, np.inf, 3]))
print(weigths)
print(conv)

x = np.linspace(0, 10, 100)
plt.plot(x, model(x, weigths[0] , weigths[1], weigths[2]), color="red")
plt.show()