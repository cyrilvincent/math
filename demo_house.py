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
plt.show()

print(f(20))

# Facile, refaire le tp en filtrant les points < 200
# Calculer la std sur les tarifs/m²
# Difficile, filtrer les appartement > 3 std et out recalculer
