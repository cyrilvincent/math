import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/house/house.csv")
df["loyer_m2"] = df.loyer / df.surface
df.to_html("data/house/house.html")
print(df.describe())

df = df[df.surface < 200]
mean = np.mean(df.loyer)
std = np.std(df.loyer)
df = df[df["loyer"] < mean + 3 * std]

plt.scatter(df.surface, df["loyer"])
plt.show()

