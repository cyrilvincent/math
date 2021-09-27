import csv

loyers = []
surfaces = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyer = float(row["loyer"])
        loyers.append(loyer)
        surfaces.append(float(row["surface"]))
print(loyers)
print(surfaces)

# TP
# Afficher dans maptplotlib le nuage de points x = surfaces, y = loyers
# Rendre le diagramme "pretty"
# Calculer le loyer moyen, surface moyenne => sum()/len()