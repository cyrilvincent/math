# Charger avec Pandas heartdisease
# y = num
# x le dataframe tout sauf num
# Fit les polynomes de degrés 1 à 10
# Bonus : idem cancer
# Critiquer le résultat pour un degrés de polynome important

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import sklearn.neural_network as nn
import sklearn.preprocessing as preprocess
import sklearn.pipeline as pipe
import sklearn.preprocessing as pp

dataframe = pd.read_csv("data/breast-cancer/data.csv",index_col="id",na_values=".")
y = dataframe.diagnosis
x = dataframe.drop("diagnosis",1)

for i in range(1,10):
    model = pipe.make_pipeline(pp.PolynomialFeatures(i), lm.Ridge())
    model.fit(x, y)
    print(i, model.score(x, y))
