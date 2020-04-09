import csv
import numpy as np
res = []
with open("mesures.csv") as f:
    for row in list(csv.reader(f))[1:]:
        row = [float(x) for x in row]
        res.append(row)
np.savez("mesures.npz", mesures = np.array(res))
data = np.load("mesures.npz")
mesures = data["mesures"]
print(mesures)
