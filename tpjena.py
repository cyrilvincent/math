import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/jena/jena_filtered.csv")
# print(dataframe.describe()["wv (m/s)"])
#
# dataframe = dataframe[5::6]
# wv = dataframe['wv (m/s)']
# bad_wv = wv == -9999.0
# wv[bad_wv] = 0.0
# dataframe.to_csv("data/jena/jena_filtered.csv", index=False)

# Fourier Transform
fft = np.fft.fft(dataframe['T (degC)'])
f_per_dataset = np.arange(0, len(fft))
n_samples_h = len(dataframe['T (degC)'])
hours_per_year = 24*365.2524
years_per_dataset = n_samples_h/hours_per_year
f_per_year = f_per_dataset/years_per_dataset
plt.step(f_per_year, np.abs(fft))
plt.xscale('log')
plt.xlim([0.1, max(plt.xlim())])
plt.xticks([1, 365.2524], labels=['1/Year', '1/day'])
_ = plt.xlabel('Frequency (log scale)')
plt.show()
# Les températures sont en fréquence identiques tous les 1j et les 1 ans

N = 24*7
conv = np.convolve(dataframe["T (degC)"], np.ones(N)/N)
print(conv)
plt.plot(dataframe["Date Time"][:365*5*24:24], dataframe["T (degC)"][:365*5*24:24])
plt.plot(dataframe["Date Time"][:365*5*24:24], conv[:365*5*24:24])
plt.show()

# Afficher les T et les P dans des subplots
# describe
