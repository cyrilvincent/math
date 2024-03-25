import matplotlib.pyplot as plt
import numpy as np

dict = np.load("data/house/house.npz")
print(dict.keys())
surface = dict["np_surfaces"]
loyer = dict["np_loyers"]
print(loyer)

plt.scatter(surface, loyer)
plt.show()

# Afficher le max, min de surface et loyer
# Créer le tableau loyer_per_m2
# Afficher loyer_per_m2 dans un subplot
# Filtrer les données pour ne garder que les surfaces < 200
# Bonus : Mettre tout celà dans des fonctions avec de sparamètres réutilisables

