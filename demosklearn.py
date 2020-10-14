import numpy as np
import pandas
import sklearn.linear_model as lm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import matplotlib.pyplot as plt
import sklearn.model_selection as ms

data = pandas.read_csv("data/house/house.csv")
x = data.surface.values.reshape(-1,1)
y = data.loyer

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

#model = lm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(3), lm.Ridge())
model.fit(xtrain, ytrain)

print(model.score(xtest, ytest))

plt.scatter(data.surface, data.loyer)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1,1)))
plt.show()

