import numpy as np
import matplotlib.pyplot as plt

dict = np.load("data/mesures/mesures.npz")
print(dict.keys())
t = dict["t"]
vm = dict["vm"]
vt = dict["vt"]

plt.subplot(211)
plt.plot(t, vm)
plt.plot(t, vt, color="red")


default = np.abs(vm - vt)
plt.subplot(212)
plt.plot(t, default)

plt.show()

filtre = default > 1
errors = default[filtre]
t_errors = t[filtre]
print(list(zip(t_errors, errors)))


# Afficher un plot t / vm et t / vt en superposé
# default = |vm - vt|
# Afficher les defauts dans un subplot
# Filtrer les defauts |vm - vt| > 1


