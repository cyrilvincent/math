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

#model = lm.LinearRegression()
for i in range(1,10):
    model = pipe.make_pipeline(pp.PolynomialFeatures(i), lm.Ridge())
    model.fit(x, y)
    #print(model.coef_, model.intercept_)
    #print(model.predict(x))
    print(i, model.score(x, y))



plt.scatter(dataframe.surface, y)
plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1, 1)))
plt.show()