import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
plt.scatter(dataframe.surface, dataframe.loyer)

slope, intercept, r_value, p_value, std_err = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, r_value, p_value, std_err)

def f(x):
    return slope * x + intercept

x = np.arange(400)
plt.plot(x, f(x), color="green")


print(f(20))

dataframe = dataframe[dataframe.surface < 200]
slope, intercept, r_value, p_value, std_err = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, r_value, p_value, std_err)
x = np.arange(200)
plt.plot(x, f(x), color="red")
plt.show()

tarif_par_m2 = dataframe.loyer / dataframe.surface
std = np.std(tarif_par_m2)
print(std)

dataframe_filtre = dataframe[np.abs(f(dataframe.surface) - dataframe.loyer) < 3 * std * dataframe.surface]
plt.scatter(dataframe_filtre.surface, dataframe_filtre.loyer)
slope, intercept, r_value, p_value, std_err = stats.linregress(dataframe_filtre.surface, dataframe_filtre.loyer)
print(slope, intercept, r_value, p_value, std_err)
x = np.arange(200)
plt.plot(x, f(x), color="red")
plt.show()

# Facile, refaire le tp en filtrant les points < 200
# Calculer la std sur les tarifs/m²
# Difficile, filtrer les appartement > 3 std et tout recalculer
