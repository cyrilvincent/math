# Dans le répertoire data/mesures
# Inspirez vous de housedemo pour lire mesures.csv
# Afficher les 4 colonnes en 2x2

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data/mesures/mesures.csv") as f:
    reader = csv.DictReader(f)
    t = []
    at = []
    vt = []
    am = []
    vm = []
    for row in reader:
        t.append(float(row["T"]))
        at.append(float(row["AT"]))
        vt.append(float(row["VT"]))
        am.append(float(row["AM"]))
        vm.append(float(row["VM"]))
    t = np.array(t)
    at = np.array(at)
    am = np.array(am)
    vt = np.array(vt)
    vm = np.array(vm)

ferror = lambda x1, x2: np.abs(x1 - x2)
ferror2 = lambda x1, x2: (x1 - x2) ** 2
adif = ferror(at, am)
# adif = np.abs(at - am)
vdif = ferror(vt, vm)
# vdif = np.abs(vt - vm)

plt.subplot(321)
plt.xlabel("Temps")
plt.ylabel("AT")
plt.plot(t, at)
plt.subplot(322)
plt.plot(t, vt)
plt.subplot(323)
plt.plot(t, am)
plt.subplot(324)
plt.plot(t, vm)
plt.subplot(325)
plt.plot(t, adif)
plt.subplot(326)
plt.plot(t, vdif)
plt.show()

filter = np.abs(at - am) > 1
afilter = am[filter]
tfilter = t[filter]
print(list(zip(tfilter, afilter)))

filter = ferror(vt, vm) > 1
vfilter = vm[filter]
t2filter = t[filter]
vtfilter = vt[filter]
print(list(zip(t2filter, vfilter, vtfilter)))

# TP Afficher les erreurs
# ferreur = |courbe theorique - courbe mesurée| > bruit = 1v ou 1a
# ferreur2 = (courbe theorique - courbe mesurée)² > bruit
# Afficher les erreurs dans matplotlib
# Créer des tableaux numpy contenant l'index des erreurs et les valeurs : filtrage (T, AM, VM)
# Afficher ces tableaux dans un print
# Bonus : refaire l'exo en chargeant mesures.npz