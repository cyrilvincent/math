import sklearn.linear_model as lm
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe

dataframe = pandas.read_csv("data/house/house.csv")
x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

#model = lm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(3), lm.Ridge())
model.fit(x, y)
print(model.score(x, y))

plt.scatter(dataframe.surface, y)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1, 1)))
plt.show()