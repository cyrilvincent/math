import sklearn.linear_model as lm
import pandas
import matplotlib.pyplot as plt
import numpy as np

dataframe = pandas.read_csv("data/house/house.csv")
x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

model = lm.LinearRegression()
model.fit(x, y)
print(model.coef_, model.intercept_)
print(model.score(x, y))

plt.scatter(dataframe.surface, y)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1, 1)))
plt.show()