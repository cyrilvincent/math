import csv
import matplotlib.pyplot as plt

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyers.append(float(row["loyer"]))
        surfaces.append(float(row["surface"]))

plt.scatter(surfaces, loyers)
plt.show()