# pip install scikit-learn
import sklearn.linear_model as lm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("data/house/house.csv")

std = np.std(dataframe.loyer)
avg = np.mean(dataframe.loyer)
dataframe = dataframe[dataframe.surface < 200]
dataframe = dataframe[dataframe.loyer < avg + 3 * std]

print(len(dataframe.surface))
x = dataframe.surface.values.reshape(-1, 1) # surface = shape(534) reshape(534,1) reshape(-1, 1)
y = dataframe.loyer

model = lm.LinearRegression()

model.fit(x, y)

predicted = model.predict(np.arange(10, 200).reshape(-1, 1))

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(10, 200), predicted, color="red")
plt.show()
