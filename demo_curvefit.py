import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

np.random.seed(0)
noise = 1
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5*x * np.sin(0.7 * x) + 2 + delta

x = np.linspace(0,100,1000)
y = f(x)

# f(x) = ax3 + bx² + cx + d
model2 = lambda x,a,b,c: a*x**2 + b*x + c
model3 = lambda x,a,b,c,d: a*x**3 + b*x**2 + c*x + d
model4 = lambda x,a,b,c,d,e: a*x**4 + b*x**3 + c*x**2 + d*x +e
model_trigo = lambda x,a,b,c: a*x * np.sin(b*x) + c 
# g(x) = ax * sin(bx) + c
# h(x) = polynome de degré 4, ou 2
# Reprise à 13h


weigth2, conv2 = opt.curve_fit(model2, x, y)
weigth3, conv3 = opt.curve_fit(model3, x, y)
weigth4, conv4 = opt.curve_fit(model4, x, y)
weigth_trigo, conv_trigo = opt.curve_fit(model_trigo, x, y)
print(weigth_trigo)
print(conv_trigo)
a2,b2,c2 = weigth2
a3,b3,c3,d3 = weigth3
a4,b4,c4,d4,e4 = weigth4
a,b,c = weigth_trigo

plt.scatter(x, y)
plt.plot(x, model2(x,a2,b2,c2), color="red")
plt.plot(x, model3(x,a3,b3,c3,d3), color="green")
plt.plot(x, model4(x,a4,b4,c4,d4,e4), color="yellow")
plt.plot(x, model_trigo(x,a,b,c), color="blue")
plt.show()
