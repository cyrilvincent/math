import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import scipy.integrate as integrate

np.random.seed(0)
noise = 5

def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta # axsin(bx)

x = np.arange(0,10,0.1)
y = f(x)

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

weight2, conv2 = opt.curve_fit(poly2, x, y)
print(weight2)
print(conv2)

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

weight3, conv3 = opt.curve_fit(poly3, x, y)
print(weight3)
print(conv3)

def poly4(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e

weight4, conv4 = opt.curve_fit(poly4, x, y)
print(weight4)
print(conv4)

def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

weightxsinx, convxsinx = opt.curve_fit(xsinx, x, y, bounds=[(0,0,1), (5, 1, 3)])
print(weightxsinx)
print(convxsinx)

def diff(x):
    return np.abs(xsinx(x, weightxsinx[0], weightxsinx[1], weightxsinx[2]) - poly4(x, weight4[0], weight4[1], weight4[2], weight4[3], weight4[4]))

area, error = integrate.quad(diff, 0, 7)
print(area, error)

plt.scatter(x, y, label="data")
plt.plot(x, poly2(x, weight2[0], weight2[1], weight2[2]), color="red", label="poly2")
plt.plot(x, poly3(x, weight3[0], weight3[1], weight3[2], weight3[3]), color="blue", label="poly3")
plt.plot(x, poly4(x, weight4[0], weight4[1], weight4[2], weight4[3], weight4[4]), color="green", label="poly4")
plt.plot(x, xsinx(x, weightxsinx[0], weightxsinx[1], weightxsinx[2]), color="maroon", label="xsinx")
plt.legend()
plt.show()

plt.plot(x, diff(x))
plt.show()