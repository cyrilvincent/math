import matplotlib.pyplot as plt
import numpy as np

dict = np.load("data/house/house.npz")
print(dict.keys())
surface = dict["np_surfaces"]
loyer = dict["np_loyers"]
loyer_per_m2 = loyer / surface
np.savez("data/house/house2.npz", loyer_per_m2=loyer_per_m2)

print(np.min(surface), np.max(loyer))
x = ["min loyer", "max loyer"]

plt.subplot(211)
plt.scatter(surface, loyer)
plt.subplot(212)
plt.scatter(surface, loyer_per_m2)
plt.show()

filtre = surface < 200
print(filtre)
surface_filtre = surface[filtre]
loyer_filtre = loyer[filtre]
loyer_per_m2_filtre = loyer_per_m2[filtre]


plt.subplot(211)
plt.scatter(surface_filtre, loyer_filtre)
plt.subplot(212)
plt.scatter(surface_filtre, loyer_per_m2_filtre)
plt.show()

# Afficher le max, min de surface et loyer
# Créer le tableau loyer_per_m2
# Afficher loyer_per_m2 dans un subplot
# Filtrer les données pour ne garder que les surfaces < 200
# Bonus : Mettre tout celà dans des fonctions avec de sparamètres réutilisables

