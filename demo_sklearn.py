import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn.neural_network as neural
import sklearn.model_selection as ms
import sklearn.neighbors as nn

df = pd.read_csv("data/house/house.csv")

x = df.surface.values.reshape(-1, 1)
y = df.loyer

np.random.seed(0)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

# model = lm.LinearRegression()
# model = neural.MLPRegressor(hidden_layer_sizes=(20,20))
model = nn.KNeighborsRegressor()
model.fit(xtrain, ytrain)

x2 = np.arange(400).reshape(-1, 1)
predicted = model.predict(x2)

score = model.score(xtest, ytest)
print(score)
# print(model.coef_, model.intercept_)
# print(model.coefs_)

plt.scatter(df.surface, y)
plt.plot(x2, predicted, color="red")
plt.show()