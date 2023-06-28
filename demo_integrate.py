import scipy.integrate
import numpy as np

def fn(x, a, b, c):
    return a * x * np.sin(b * x) + c

a = 2.5
b = 0.7
c = 10
I = scipy.integrate.quad(fn, 0, 10, args=(a,b,c))
print(I)