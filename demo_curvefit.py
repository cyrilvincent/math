import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as integrate

np.random.seed(0)
noise = 1
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5*x * np.sin(0.7 * x) + 2 + delta

x = np.linspace(0,10,100)
y = f(x)

# f(x) = ax3 + bx² + cx + d
model2 = lambda x,a,b,c: a*x**2 + b*x + c
model3 = lambda x,a,b,c,d: a*x**3 + b*x**2 + c*x + d


weigth2, conv2 = opt.curve_fit(model2, x, y)
print(weigth2)
print(conv2)
a2 = weigth2[0]
b2 = weigth2[1]
c2 = weigth2[2]
weigth3, conv3 = opt.curve_fit(model3, x, y)
print(weigth3)
print(conv3)
a3 = weigth3[0]
b3 = weigth3[1]
c3 = weigth3[2]
d3 = weigth3[3]



plt.scatter(x, y)
plt.plot(x, model3(x, a3, b3, c3, d3), color="red")
plt.plot(x, model2(x, a2, b2, c2), color="green")
plt.show()
