import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.ensemble as en

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]

x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

model = lm.LinearRegression()
model.fit(x, y)
print(model.score(x, y))
predicted = model.predict(np.arange(200).reshape(-1, 1))

plt.scatter(x, y)
plt.plot(np.arange(200).reshape(-1, 1), predicted, color="red")
plt.show()

dataframe= pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", axis=1)
model = lm.LinearRegression()
model.fit(x, y)
print(model.score(x, y))
predicted = model.predict(x)
print(model.coef_)