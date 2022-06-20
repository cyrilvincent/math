import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyer = float(row["loyer"])
        loyers.append(loyer)
        surfaces.append(float(row["surface"]))

print(surfaces)
print(loyers)

# Afficher le nuage de points x: surfaces, y: loyers