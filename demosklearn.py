import sklearn.linear_model as lm
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.model_selection as ms

dataframe = pandas.read_csv("data/house/house.csv")
x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

#model = lm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(3), lm.Ridge())
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

plt.scatter(dataframe.surface, y)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1, 1)))
plt.show()