import numpy as np
import matplotlib.pyplot as plt

dict = np.load("data/jena/jena.npz")
print(list(dict.keys()))
p = dict["p"]
t = dict["t"]
print(p.shape)
x = np.arange(70075)

plt.plot(x, t)
plt.show()

# TP
# Afficher dans 2 diagrammes les temperatures et pressions
# Calculer la temperature min, max
# Afficher les temperatures par jour (prendre une temperature sur 24)
# Idem, mais commencer par la temperature de midi
# Afficher les temperatures de la 1ère année uniquement
# Calculer le min et max de temperature de l'année 1, 2 et 3
# Créer le vecteur tp qui est t/p

