import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# pip install scipy

dataframe = pd.read_csv("data/house/house.csv")
dataframe_filter = dataframe[dataframe.surface < 200]

avg = np.mean(dataframe_filter.loyer / dataframe_filter.surface)
std = np.std(dataframe_filter.loyer / dataframe_filter.surface)
print(avg, std)

slope, intercept, r_value, p_value, std_err = stats.linregress(dataframe_filter.surface, dataframe_filter.loyer)
print(slope, intercept, r_value, p_value, std_err)
# f(x) = 41x - 283
# f(x) = 34x + 122
f = lambda x : slope * x + intercept

std_filter = np.abs(f(dataframe_filter.surface) - dataframe_filter.loyer) < 3 * std * dataframe_filter.surface
dataframe_filter2 = dataframe_filter[std_filter]

slope, intercept, r_value, p_value, std_err = stats.linregress(dataframe_filter2.surface, dataframe_filter2.loyer)
print(slope, intercept, r_value, p_value, std_err)

plt.scatter(dataframe_filter2.surface, dataframe_filter2.loyer)
plt.plot(np.arange(200), f(np.arange(200)), color='red')
plt.show()

# Interpréter le résultat
# Filtrer les data < 200m²
# Recalculer la regression
# Bonus : loyer_per_m2 recalculer le std, virer les points > 3*std
# Recalculer la regression
# Bonus : Heart disease calculer la regression pour x = age, y = chol

# Courbe U
# Polynome de degré 2 ou 3
# f(x) = ax² + bx + c
# Curvefit ax + b
# Curvefit  f(x) = ax² + bx + c
# Bonus 3ème degré
# Afficher les courbes
