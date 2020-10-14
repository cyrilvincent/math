import numpy as np
import pandas
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

data = pandas.read_csv("data/house/house.csv")
x = data.surface.values.reshape(-1,1)
y = data.loyer

model = lm.LinearRegression()
model.fit(x, y)
print(model.intercept_, model.coef_)

plt.scatter(data.surface, data.loyer)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1,1)))
plt.show()

