# Avec pandas lire data/mesures/mesures.csv
# Mettre la colonne T en index avec la paramètre index_col
# Afficher dans matplotlib les colonnes AM & VM
# Ajouter la colonne PC (Puissance Calculée) = AM * VM
# LA colonne VT correspond aux données théoriques = Créer la colonne VDiff = np.abs(VM - VT)
# Afficher VT & VDiff

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/mesures/mesures.csv", index_col="T")

df["PC"] = df["AM"] * df["VM"]
df["VDiff"] = np.abs(df["VM"] - df["VT"])
print(df)

plt.subplot(2,2,1)
plt.plot(df.index, df["AM"])
plt.subplot(2,2,2)
plt.plot(df.index, df["VT"], color="red")
plt.plot(df.index, df["VM"])
plt.subplot(2,2,3)
plt.plot(df.index, df["PC"])
plt.subplot(2,2,4)
plt.plot(df.index, df["VDiff"])
plt.show()