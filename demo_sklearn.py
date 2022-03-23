import sklearn
import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")

print(sklearn.__version__)
model = lm.LinearRegression()
model.fit(dataframe.surface.values.reshape(-1, 1), dataframe.loyer)
predicted = model.predict(np.arange(400).reshape(-1, 1))
print(model.coef_, model.intercept_)

score = model.score(dataframe.surface.values.reshape(-1, 1), dataframe.loyer)
print(f"Score: {score}")


plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(400), predicted)
plt.show()


