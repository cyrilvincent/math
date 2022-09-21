import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

dataframe = pd.read_csv("data/house/house.csv")
plt.scatter(dataframe.surface, dataframe.loyer)

f2 = lambda x,a,b,c : a*x**2 + b*x + c

res, conv = opt.curve_fit(f2, dataframe.surface, dataframe.loyer)

print(res)
print(conv)

x = np.arange(400)
plt.plot(x, f2(x, res[0], res[1], res[2]), color="red")

f3 = lambda x,a,b,c,d : a*x**3 + b*x**2 + c*x + d
res, conv = opt.curve_fit(f3, dataframe.surface, dataframe.loyer)
print(res)
print(conv)

x = np.arange(400)
plt.plot(x, f3(x, res[0], res[1], res[2], res[3]), color="green")

plt.show()
# Curvefiter une courbe en U (polynome de degré 2 puis 3)

