import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/mesures/mesures.npz")
mesures = data["mesures"]
print(mesures.shape)
plt.plot(mesures[:,4])
plt.show()

# Colonne 0 : indice de temps
# Colonne 2 : Volts (240) Theorique
# Colonne 4 : Volts (240) Mesuré
# Afficher colonne 2 et 4 en y et colonne 0 en x
# delta = 1v
# min et max de la colonne 4
# bruit_abs = |col2 - col4|
# bruit_square = (col2 - col4)²
# Trouver les index temps où |col2 - col4| > delta