import numpy as np
import matplotlib.pyplot as plt

nb = 10000
matrice = np.random.rand(nb,nb)
sommes = matrice.sum(-1)
print(sommes)
plt.scatter(range(nb), sommes)
plt.show()
plt.hist(sommes)
plt.show()

x = np.arange(-100,100)
mu = 0
sigma = 20
f = lambda x : 1/(np.sqrt(2*np.pi*pow(sigma,2))) * np.exp(-pow((x-mu),2)/(2*pow(sigma,2)))
plt.plot(x, f(x))
plt.show()

