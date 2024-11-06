import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as integrate

np.random.seed(0)
noise = 10

def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5 * x * np.sin(0.7 * x) + 2 + delta

x = np.arange(0,10,0.1)
y = f(x)

def poly2(x,a,b,c):
    return a*x**2 + b*x + c

weight2, conv2 = opt.curve_fit(poly2, x ,y)
print(weight2)
a = weight2[0]
b = weight2[1]
c = weight2[2]
print(conv2)

plt.scatter(x, y)
plt.plot(x, poly2(x, a, b, c), color="red")

def poly3(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

weight3, conv3 = opt.curve_fit(poly3, x ,y)
print(weight3)
a = weight3[0]
b = weight3[1]
c = weight3[2]
d = weight3[3]
print(conv3)

plt.plot(x, poly3(x, a, b, c, d), color="green")

def xsinx(x, a, b, c):
    return a*x * np.sin(b*x) +c

weight2, conv2 = opt.curve_fit(xsinx, x ,y)
print(weight2)
a = weight2[0]
b = weight2[1]
c = weight2[2]
print(conv2)

def abs_xsinx(x, a, b, c):
    return np.abs(xsinx(x, a, b, c))

surface = integrate.quad(abs_xsinx, 0, 10, args=(a, b, c))
print(surface)



plt.plot(x, xsinx(x, a, b, c), color="orange")
plt.show()



# TP
# Polynome degré 4
# Fitter ax sin(bx) + c
# Augmenter noise
