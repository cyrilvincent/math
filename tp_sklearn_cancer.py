import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.neighbors as nn
import sklearn.preprocessing as pp

dataframe = pd.read_csv("data/breast-cancer/data.csv", index_col="id")

y = dataframe.diagnosis
x = dataframe.drop("diagnosis", axis=1)

scaler = pp.RobustScaler()
scaler.fit(x, y)
x = scaler.transform(x)

# model = lm.LinearRegression()
model = nn.KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

predicted = model.predict(x)
print(x.shape)
print(model.score(x, y))

# print(model.coef_, model.intercept_)



