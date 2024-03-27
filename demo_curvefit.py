import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as integrate

np.random.seed(0)
noise = 10
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5*x * np.sin(0.7 * x) + 2 + delta

x = np.linspace(0,10,100)
y = f(x)

# f(x) = ax3 + bx² + cx + d
model2 = lambda x,a,b,c: a*x**2 + b*x + c
model3 = lambda x,a,b,c,d: a*x**3 + b*x**2 + c*x + d
model4 = lambda x,a,b,c,d,e: a*x**4 + b*x**3 + c*x**2 + d*x +e
model5 = lambda x,a,b,c: a*x * np.sin(b*x) + c
# Tester avec polynome du 4ème degrés
# Tester avec x sin(x) et modifiant le bruit


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
weigth4, conv4 = opt.curve_fit(model4, x, y)
print(weigth4)
print(conv4)
a4 = weigth4[0]
b4 = weigth4[1]
c4 = weigth4[2]
d4 = weigth4[3]
e4 = weigth4[4]
weigth5, conv5 = opt.curve_fit(model5, x, y, bounds=([2, 0.5, -np.inf], [3, 1, np.inf]))
print(weigth5)
print(conv5)
a5 = weigth5[0]
b5 = weigth5[1]
c5 = weigth5[2]


plt.scatter(x, y)
plt.plot(x, model3(x, a3, b3, c3, d3), color="red")
plt.plot(x, model2(x, a2, b2, c2), color="green")
plt.plot(x, model4(x, a4, b4, c4, d4,e4), color="yellow")
plt.plot(x, model5(x, a5, b5, c5), color="black")
plt.show()
