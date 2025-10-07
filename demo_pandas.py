import pandas as pd
import matplotlib.pyplot as plt
# pip install xlrd

# dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx", sheet_name="Sheet1")
print(dataframe)

dataframe = dataframe[dataframe["surface"] < 200]
dataframe["loyer_per_m2"] = dataframe["loyer"] / dataframe["surface"]

print(dataframe.describe())

dataframe.to_html("data/house/house.html")


plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.show()

