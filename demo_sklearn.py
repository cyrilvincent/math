import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.linear_model as lm
import sklearn.model_selection as ms

dataframe = pd.read_csv("data/house/house.csv")
# plt.scatter(dataframe.surface, dataframe.loyer)

x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)
# On fit sur train
# On predict et score sur test

# model = lm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(2), lm.Ridge())
model.fit(xtrain, ytrain)

predicted = model.predict(np.arange(400).reshape(-1, 1))
print(model.score(xtest, ytest))
plt.scatter(xtest, ytest)
plt.plot(np.arange(400), predicted, color="red")
plt.show()



