import csv

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        surface = float(row["surface"])
        loyer = float(row["loyer"])
        loyer_m2 = loyer / surface
        print(surface, loyer, loyer_m2)

# Afficher le nuage de point surface par loyer
# Calculer le loyer / m2 moyen
# Ecrire la lambda loyer_m2 * x
# Afficher le résulat de la fonction affine loyer_m2 en superposition