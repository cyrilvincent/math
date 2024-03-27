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

nb = len(t)
x = np.arange(nb)
plt.subplot(411)
plt.step(x, t)
plt.subplot(412)
x2 = x[11::24]
t2 = t[11::24]
plt.plot(x2, t2)
plt.subplot(413)
res = fft.fft(t)
nb_years = nb / (365*24)
f_per_years = x / nb_years
plt.plot(f_per_years, np.abs(res))
plt.xscale("log")
plt.xticks([1, 365], labels=['1/Year', '1/day'])
plt.subplot(414)
n = 24*7
conv = np.convolve(t, np.ones(n)/n)
plt.plot(x, conv[:nb])
plt.show()



