import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

dico = np.load("data/house/house.npz")
loyers = dico["np_loyers"]
surfaces = dico["np_surfaces"]
df = pd.DataFrame()
df["loyers"] = loyers
df["surfaces"] = surfaces
print(df)
mean_loyers = np.mean(df["loyers"])
std_loyers = np.std(df["loyers"])

df = df[df["surfaces"] < 200]
df = df[df["loyers"] < mean_loyers + 3 * std_loyers]

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue)

plt.scatter(df["surfaces"], df["loyers"])
plt.plot(df["surfaces"], slope * df["surfaces"] + intercept, color="red")
plt.show()