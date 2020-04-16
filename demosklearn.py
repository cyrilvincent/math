import pandas as pd
import sklearn.linear_model as sklm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data/house/house.csv")
#model = sklm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(3), sklm.Ridge())
x = data["surface"].values.reshape(-1, 1)
y = data["loyer"]

model.fit(x, y)
print(model.score(x,y))

plt.scatter(data.surface, data.loyer)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1,1)))
plt.show()