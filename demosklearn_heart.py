import numpy as np
import pandas
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.ensemble as rf

data = pandas.read_csv("data/heartdisease/dataclean.csv")
y = data.num
x = data.drop("num",1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

#model = lm.LinearRegression()
model = neighbors.KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))
