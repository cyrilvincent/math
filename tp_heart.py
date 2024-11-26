import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(df.isnull().sum())
df = df.drop(["slope", "ca", "thal"], axis=1)
mean_chol = np.mean(df.chol)
std_chol = np.std(df.chol)
df.fillna({"chol": mean_chol + (np.random.rand() - 0.5) * std_chol}, inplace=True)

df =df.dropna()
print(df.isnull().sum())
df.to_csv("data/heartdisease/dataclean.csv")




