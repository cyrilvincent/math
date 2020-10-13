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

delta = 1
vt = mesures[:,2]
vm = mesures[:,4]
ix = mesures[:,0]
print(np.min(vm), np.max(vm))

def get_mesures_errors(ix,vt,vm, filtre):
    """
    Calcul les erreurs entre VT et VM
    :param ix: index de temps
    :param vt: volt théoriques
    :param vm: volt mesurés
    :param filtre: filtre de bruit
    :return: liste de tuples (ix, vt, vm)
    """
    triplets = list(zip(ix[filtre], vt[filtre], vm[filtre]))
    return triplets

bruit_abs = np.abs(vm - vt)
bruit_square = (vm - vt) ** 2
filtre = bruit_abs > delta
res = get_mesures_errors(ix,vm,vt,filtre)
print(res)