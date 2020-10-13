import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data/covid/covid-france.txt") as f:
    reader = csv.DictReader(f)
    ix = []
    nbcas = []
    dc = []
    for row in reader:
        ix.append(float(row["ix"]))
        nbcas.append(float(row["NbCas"]))
        dc.append(float(row["DC"]))

ix = np.array(ix)
nbcas = np.array(nbcas)
dc = np.array(dc)
filtre = nbcas > 10
nbcas_filtre = nbcas[filtre]
dc_filtre = dc[filtre]
ix_filtre = ix[filtre]
letalite = dc_filtre / nbcas_filtre

#plt.yscale("log")
plt.plot(nbcas)
plt.plot(dc)
plt.show()
plt.plot(letalite)
plt.show()