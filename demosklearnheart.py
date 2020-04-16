import pandas as pd
import sklearn.linear_model as sklm
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe


data = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = data['num']
x = data.drop("num", 1)

#model = sklm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(4), sklm.Ridge())
model.fit(x, y)
print(model.score(x,y))
print(model.predict(x) > 0.5)