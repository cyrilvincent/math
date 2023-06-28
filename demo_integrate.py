from scipy.integrate import quad
import numpy as np

def fn(x, a, b, c):
    return a * x * np.sin(b * x) + c

a = 2.5
b = 0.7
c = 2
I = quad(fn, 0, 1, args=(a,b,c))
print(I)