import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("data/jena/jena_filtered.csv")
fft = np.fft.fft(df["T (degC)"])
f_per_dataset = np.arange(len(fft))
hours_per_year = 24*365.25
years_per_dataset = len(fft) / hours_per_year
f_per_year = f_per_dataset / years_per_dataset
plt.subplot(311)
plt.plot(df["T (degC)"])
plt.subplot(312)
plt.step(f_per_year, np.abs(fft))
plt.xlim([0.5, max(plt.xlim())])
plt.xticks([1, 365.25], labels=["1/year", "1/day"])
plt.xscale("log")


slope, intercept, rvalue, pvalue, stderr = stats.linregress(f_per_dataset, df["T (degC)"])
print(slope, intercept, rvalue, pvalue, stderr)

plt.subplot(313)
plt.plot(f_per_dataset * slope + intercept)

plt.show()