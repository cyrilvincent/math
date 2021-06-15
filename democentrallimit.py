import numpy as np
import matplotlib.pyplot as plt
matrice_aleatoire = np.random.rand(100,100000)
sommes = np.sum(matrice_aleatoire,0)
plt.subplot(211)
plt.scatter(range(100000), sommes)
plt.subplot(212)
plt.hist(sommes,bins=100)
print("La moyenne empirique de notre distribution est {}."
      .format(np.mean(sommes)))
print("La moyenne empirique de la variable généré par la fonction rand est {}."
      .format(np.mean(np.random.rand(100000))))
print("La déviation standard empirique de notre distribution est {}."
      .format(np.std(sommes)))
print("La déviation standard empirique de la variable généré par la fonction rand est {}."
      .format(np.std(np.random.rand(100000))))
np.quantile
plt.show()