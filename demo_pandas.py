import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# pip install openpyxl

df = pd.read_csv("data/house/house.csv",)


# df.hist(bins=50)
df["loyer_m2"] = df["loyer"] / df["surface"]

loyer_mean = np.mean(df["loyer_m2"])
loyer_std = np.std(df["loyer_m2"])
print(loyer_mean, loyer_std)

df = df[(df["loyer_m2"] < loyer_mean + 3 * loyer_std) & (df["surface"] < 200)]


print(df.describe())
plt.scatter(df["surface"], df["loyer"])
plt.show()


df.to_json("data/house/house.json", index=False, indent=4)
df.to_excel("data/house/house.xlsx", index=False)

