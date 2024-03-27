import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

dataframe = pd.read_csv("data/jena/jena_filtered.csv")
t = dataframe["T (degC)"]
print(t.describe())
t = t.values

# Prendre un t toutes les 24h, à midi
# Afficher le plot
# Appliquer une fft et afficher la partie réelle
# Refaire sans le filtre de 24h

x = np.arange(70075)
x2 = x[11::24]
t2 = t[11::24]
res = fft.fft(t)
plt.subplot(311)
plt.plot(x, t)
plt.subplot(312)
plt.plot(x2, t2)
plt.subplot(313)
plt.plot(x, np.abs(res))
plt.xscale("log")
plt.show()
