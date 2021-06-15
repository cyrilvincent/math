import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/jena/jena_climate_2009_2016.csv")
print(dataframe.describe()["wv (m/s)"])

dataframe = dataframe[5::6]
wv = dataframe['wv (m/s)']
bad_wv = wv == -9999.0
wv[bad_wv] = 0.0
dataframe.to_csv("data/jena/jena_filtered.csv", index=False)

N = 24*7
conv = np.convolve(dataframe["T (degC)"], np.ones(N)/N)
print(conv)
plt.plot(dataframe["Date Time"][:365*5*24:24], dataframe["T (degC)"][:365*5*24:24])
plt.plot(dataframe["Date Time"][:365*5*24:24], conv[:365*5*24:24])
plt.show()

# Afficher les T et les P dans des subplots
# describe
