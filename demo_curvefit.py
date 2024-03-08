import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

np.random.seed(0)
noise = 10
def f(x):
    delta = (np.random.rand(x.shape[0]) - 0.5) * noise
    return 2.5*x * np.sin(0.7 * x) + 2 + delta

x = np.linspace(0,10,100)
y = f(x)

# f(x) = ax3 + bx² + cx + d
model = lambda x,a,b,c,d: a*x**3 + b*x**2 + c*x + d
# g(x) = ax * sin(bx) + c


weigth, conv = opt.curve_fit(model, x, y) #bounds=([1,3,1], [0.1,1,2]))
print(weigth)
print(conv)
a,b,c,d = weigth

plt.scatter(x, y)
plt.plot(x, model(x,a,b,c,d), color="red")
plt.show()
