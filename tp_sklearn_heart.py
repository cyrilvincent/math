# Charger avec Pandas heartdisease
# y = num
# x le dataframe tout sauf num
# Fit les polynomes de degrés 1 à 10
# Bonus : idem cancer
# Critiquer le résultat pour un degrés de polynome important

import numpy as np
import pandas
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import sklearn.neural_network as nn
import sklearn.preprocessing as preprocess
import sklearn.pipeline as pipe
import sklearn.preprocessing as pp

data = pandas.read_csv("data/heartdisease/dataclean.csv")
y = data.num
x = data.drop("num",1)

np.random.seed(1)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

for i in range(1,4):
    modelpp = pp.PolynomialFeatures(i)
    model = pipe.make_pipeline(modelpp, lm.Ridge())
    model.fit(xtrain, ytrain) #NE VOIT JAMAIS XTEST et YTEST
    print(i, model.score(xtrain, ytrain))
    print(i, model.score(xtest, ytest))
