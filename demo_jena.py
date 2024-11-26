import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/jena/jena_filtered.csv")

fft = np.fft.fft(df["T (degC)"])
f_per_dataset = np.arange(len(fft))
hours_per_year = 24*365.25
years_per_dataset = len(f_per_dataset)/hours_per_year
f_per_year = f_per_dataset/years_per_dataset
plt.step(f_per_year, np.abs(fft))
plt.xlim([0.5, max(plt.xlim())])
plt.xticks([1, 365.25], labels=["1/year", "1/day"])
plt.xscale("log")
plt.show()