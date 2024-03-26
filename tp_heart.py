import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
print(dataframe.describe().T)

ok = dataframe[dataframe.num == 0]
ko = dataframe[dataframe.num == 1]

print(ok.describe().T)
print(ko.describe().T)

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop(["ca", "thal", "slope"], axis=1)
print(dataframe.describe().T)
# Strategie 1
dataframe1 = dataframe.dropna()
print(dataframe1.describe().T)
# Strategie 2
mean = np.mean(dataframe.chol)
std = np.std(dataframe.chol)
dataframe.chol = dataframe.chol.fillna(mean + (np.random.rand() - 0.5) * 2 * std)
dataframe2 = dataframe.dropna()
print(dataframe2.describe().T)