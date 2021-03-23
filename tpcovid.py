import pandas
import numpy as np
import matplotlib.pyplot as plt

dataframe = pandas.read_csv("data/covid/covid-france.txt")
# print(dataframe)

plt.plot(dataframe["nb"], dataframe.NbCas)
plt.plot(dataframe["nb"], dataframe.DC)
plt.yscale("log")
plt.show()

dataframe_filtree = dataframe[dataframe.DC > 0]
letalite = dataframe_filtree.NbCas / dataframe_filtree.DC
print(letalite)
dataframe_filtree["letalite"] = letalite
print(dataframe_filtree)
# print(np.mean(letalite))
dataframe_filtree.to_json("data/covid/covid.json")

# Avec pandas charger covid-france.txt ou covid.xlsx
# Afficher un matplotlib en x=ix en y=nbcas et dc
# plt.yscale("log")
# letalite = dc / nbcas
    # Filtrer les données pour ix > 42
    # dataframe.dc dataframe["dc"]
# Sauvegarder la letalité en json
# dataframe["letalite"] = letalite
