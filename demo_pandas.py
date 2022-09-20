import pandas as pd
import matplotlib.pyplot as plt
# openpyxl

#dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx", "Toto")

dataframe = dataframe[dataframe.surface < 200]
print(dataframe)

dataframe.to_csv("data/house/house2.csv", index=False)
dataframe.to_html("data/house/house.html", index=False)

print(dataframe.describe().T)

plt.scatter(dataframe.surface, dataframe["loyer"])
plt.show()