import csv
import numpy as np
with open("mesures.csv") as f:
    reader = list(csv.reader(f))
print(reader[1:])
np.savez("mesures.npz", mesures = np.array(reader[1:]))
data = np.load("mesures.npz")
mesures = data["mesures"]
print(mesures)
