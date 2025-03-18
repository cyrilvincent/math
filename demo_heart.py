import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
print(dataframe)
print(dataframe.isnull().sum())
dataframe = dataframe.drop(["slope", "ca", "thal"], axis=1)
print(dataframe.isnull().sum())
mean_chol = np.nanmean(dataframe.chol) # dataframe.chol.mean()
std_chol = dataframe.chol.std()
print(mean_chol, std_chol)
dataframe.chol.hist(bins=10)
dataframe.fillna({"chol": int(mean_chol + (np.random.rand() - 0.5) * std_chol)}, inplace=True)
print(dataframe.isnull().sum())
dataframe = dataframe.dropna()
dataframe.to_csv("data/heartdisease/dataclean.csv")
plt.show()

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]

print(ok.chol.mean(), ko.chol.mean())
print(ok.chol.std(), ko.chol.std())

print(ok.thalach.mean(), ko.thalach.mean())
print(ok.thalach.std(), ko.thalach.std())