import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", 1)

benin_filter = y == 0
malin_filter = y == 1

print(x[benin_filter].chol.describe())
print(x[malin_filter].chol.describe())

print(x[benin_filter].sex.describe())
print(x[malin_filter].sex.describe())
