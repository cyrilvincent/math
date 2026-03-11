import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

noise = 10
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.arange(0,10,0.1)
y = f(x)

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def poly4(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e

def xsinx(x, a, b, c):
    return a * x * np.sin(b * x) + c

result3 = opt.curve_fit(poly3, x ,y)
a = result3[0][0]
b = result3[0][1]
c = result3[0][2]
d = result3[0][3]
print(result3)

plt.scatter(x, y)
# plt.plot(x, poly3(x, a, b, c, d))

result4 = opt.curve_fit(poly4, x ,y) #, bounds=[(-np.inf, np.inf), (0, 1)])
a = result4[0][0]
b = result4[0][1]
c = result4[0][2]
d = result4[0][3]
e = result4[0][4]
# plt.plot(x, poly4(x, a, b, c, d, e))

result_xsin = opt.curve_fit(xsinx, x ,y)
a = result_xsin[0][0]
b = result_xsin[0][1]
c = result_xsin[0][2]
print(a, b, c)
plt.plot(x, xsinx(x, a, b, c), color="red")
plt.show()
