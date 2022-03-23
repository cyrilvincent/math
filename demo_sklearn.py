import sklearn
import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.model_selection as ms

dataframe = pd.read_csv("data/house/house.csv")

np.random.seed(1)
x = dataframe.surface.values.reshape(-1, 1)
y = dataframe.loyer
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y,train_size=0.8, test_size=0.2 )

print(sklearn.__version__)
model = lm.LinearRegression()
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(f"Score: {score}")
# for i in range(2, 9):
#     model = pipe.make_pipeline(pp.PolynomialFeatures(i), lm.Ridge())
#     model.fit(xtrain, ytrain)
#     score = model.score(xtest, ytest)
#     print(f"Score {i}: {score}")


predicted = model.predict(np.arange(400).reshape(-1, 1))
# print(model.coef_, model.intercept_)




plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(np.arange(400), predicted)
plt.show()


