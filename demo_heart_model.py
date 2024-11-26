import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option('display.width', 1000)

df = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
print(df.describe())

ok = df[df.num == 0]
ko = df[df.num == 1]

print(ok.describe())
print(ko.describe())

print(df.corr())
plt.matshow(df.corr())
plt.show()