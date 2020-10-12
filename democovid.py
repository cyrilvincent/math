import csv
import matplotlib.pyplot as plt

with open("data/covid/covid-france.txt") as f:
    reader = csv.DictReader(f)
    ix = []
    nbcas = []
    dc = []
    for row in reader:
        ix.append(float(row["ix"]))
        nbcas.append(float(row["NbCas"]))
        dc.append(float(row["DC"]))

plt.yscale("log")
plt.plot(ix, nbcas)
plt.plot(ix, dc)
plt.show()