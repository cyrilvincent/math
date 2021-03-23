import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100)
mu = 0
sigma = 20

f = lambda x : 1/(np.sqrt(2*np.pi*np.power(sigma,2))) * np.exp(-np.power((x-mu),2)/(2*np.power(sigma,2)))

y = f(x)
plt.plot(x, y)
plt.show()