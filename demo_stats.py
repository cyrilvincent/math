import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")

print(np.mean(dataframe.loyer),np.std(dataframe.loyer),np.median(dataframe.loyer),np.quantile(dataframe.loyer, [0.25,0.75]))
print(np.mean(dataframe.surface),np.std(dataframe.surface),np.median(dataframe.surface),np.quantile(dataframe.surface, [0.25,0.75]))
dataframe.surface.hist(bins=20)
plt.show()