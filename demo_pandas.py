import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
print(dataframe["loyer"])
print(dataframe.surface)
print(dataframe.describe())
dataframe["loyer_per_m2"] = dataframe["loyer"] / dataframe["surface"]
print(dataframe)
dataframe = dataframe[dataframe.surface < 200]
dataframe.to_html("data/house/house.html")
# pip install lxml
dataframe.to_xml("data/house/house.xml")
# pip install openpyxl
dataframe.to_excel("data/house/house.xlsx", index=False)

a1 = np.array([1,2,3,np.nan])
print(np.mean(a1), np.nanmean(a1))