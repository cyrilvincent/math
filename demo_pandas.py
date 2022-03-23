import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import scipy.optimize as opt

dataframe = pd.read_csv("data/house/house.csv")
#dataframe = pd.read_excel("data/house/house.xlsx", index_col="id")
# with sqlite3.connect("data/house/house.db3") as conn:
#     dataframe = pd.read_sql("select * from house", conn)

f2 = lambda x, a, b, c: a * x ** 2 + b * x + c

weights, conv = opt.curve_fit(f2, dataframe.surface, dataframe.loyer)
print(weights)
print(conv)

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(9, 400), f2(np.arange(9, 400), weights[0], weights[1], weights[2]), color="red")
plt.show()

dataframe = dataframe[dataframe.surface < 200]

loyers_serie = dataframe.loyer
print(loyers_serie)

print(dataframe.describe().T)

slope, intercept, rvalue, pvalue, _ = stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept)
f1 = lambda x : slope * x + intercept

avg = np.mean(dataframe.loyer / dataframe.surface)
std = np.std(dataframe.loyer / dataframe.surface)




plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(9, 200), f1(np.arange(9, 200)), color="green")
plt.show()

std_filter = np.abs(f1(dataframe.surface) - dataframe.loyer) < 3 * std * dataframe.surface
dataframe_filter = dataframe[std_filter]
slope2, intercept2, rvalue2, pvalue2, _ = stats.linregress(dataframe_filter.surface, dataframe_filter.loyer)
print(slope2, intercept2)
f = lambda x : slope2 * x + intercept2

plt.scatter(dataframe_filter.surface, dataframe_filter.loyer)
plt.plot(np.arange(9, 200), f(np.arange(9, 200)), color="red")
plt.show()




# Afficher nuage de points surfaces / loyers
# Calculer et afficher la regression lineaire
# Enlever les surfaces > 200
# Recalculer la regression
# Enlever les points dont la distance avec la droite > |f(x + 3 * std) - f(x)|
# Recalculer la regression