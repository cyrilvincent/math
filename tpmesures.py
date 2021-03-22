# Dans le répertoire data/mesures
# Inspirez vous de housedemo pour lire mesures.csv
# Afficher les 4 colonnes en 2x2

import csv
import matplotlib.pyplot as plt

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
plt.subplot(221)
plt.xlabel("Temps")
plt.ylabel("AT")
plt.plot(t, at)
plt.subplot(222)
plt.plot(t, vt)
plt.subplot(223)
plt.plot(t, am)
plt.subplot(224)
plt.plot(t, vm)
plt.show()