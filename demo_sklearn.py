# pip install scikit-learn
import sklearn
import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
np.random.seed(1)
x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

print(sklearn.__version__)
model = lm.LinearRegression()
model.fit(x, y)
print(model.coef_, model.intercept_)
score = model.score(x, y)
print(f"Score: {score}")


predicted = model.predict(np.arange(400).reshape(-1, 1))

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(400), predicted, color="red")
plt.show()