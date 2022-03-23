import sklearn
import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe

dataframe = pd.read_csv("data/house/house.csv")

print(sklearn.__version__)
# model = lm.LinearRegression()
for i in range(2, 9):
    model = pipe.make_pipeline(pp.PolynomialFeatures(i), lm.Ridge())
    model.fit(dataframe.surface.values.reshape(-1, 1), dataframe.loyer)
    score = model.score(dataframe.surface.values.reshape(-1, 1), dataframe.loyer)
    print(f"Score {i}: {score}")


predicted = model.predict(np.arange(400).reshape(-1, 1))
# print(model.coef_, model.intercept_)




plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(400), predicted)
plt.show()


