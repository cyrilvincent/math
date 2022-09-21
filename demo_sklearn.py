import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
plt.scatter(dataframe.surface, dataframe.loyer)

x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

model = lm.LinearRegression()
model.fit(x, y)

predicted = model.predict(np.arange(400).reshape(-1, 1))
plt.plot(np.arange(400), predicted, color="red")
plt.show()



