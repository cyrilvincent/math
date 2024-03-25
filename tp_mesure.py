import numpy as np

dict = np.load("data/mesures/mesures.npz")
print(dict.keys())
t = dict["t"]
vm = dict["vm"]
vt = dict["vt"]

# Afficher un plot t / vm et t / vt en superposé
# default = |vm - vt|
# Afficher les defauts dans un subplot
# Filtrer les defauts |vm - vt| > 1


