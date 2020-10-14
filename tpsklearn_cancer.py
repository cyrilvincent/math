import numpy as np
import pandas
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors
import matplotlib.pyplot as plt
import sklearn.model_selection as ms

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
y = data.diagnosis
x = data.drop("diagnosis",1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

#model = lm.LinearRegression()
model = neighbors.KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))
print((model.predict(xtest) - ytest).values)


