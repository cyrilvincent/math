import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# pip install scipy

dataframe = pd.read_csv("data/house/house.csv")

slope, intercept, r_value, p_value, std_err = stats.linregress(dataframe.surface, dataframe.loyer)

print(slope, intercept, r_value, p_value, std_err)
# f(x) = 41x - 283
f = lambda x : slope * x + intercept

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(400), f(np.arange(400)), color='red')
plt.show()

# Interpréter le résultat
# Filtrer les data < 200m²
# Recalculer la regression
# Bonus : loyer_per_m2 recalculer le std, virer les points > 3*std
# Recalculer la regression
# Bonus : Heart disease calculer la regression pour x = age, y = chol

