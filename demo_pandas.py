import pandas as pd
import sqlite3

#dataframe = pd.read_csv("data/house/house.csv")
#dataframe = pd.read_excel("data/house/house.xlsx", index_col="id")
with sqlite3.connect("data/house/house.db3") as conn:
    dataframe = pd.read_sql("select * from house", conn)
print(dataframe)

dataframe = dataframe[dataframe.loyer < 200]

loyers_serie = dataframe.loyer
print(loyers_serie)

print(dataframe.describe().T)

# Afficher nuage de points surfaces / loyers
# Calculer et afficher la regression lineaire
# Enlever les surfaces > 200
# Recalculer la regression
# Enlever les points dont la distance avec la droite > |f(x + 3 * std) - f(x)|
# Recalculer la regression