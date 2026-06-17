# Charger data/heartdisease/data_cleaned_up.csv
# dataframe ok pour num==0
# dataframe ko pour num==1
# mean, std sur les colonnes importantes

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# pip install openpyxl

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("data/heartdisease/data_cleaned_up.csv", na_values=".")
print(df.describe())

ok = df[df["num"] == 0]
ko = df[df["num"] == 1]

print(ok.describe())
print(ko.describe())

print(df.corr())