import numpy as np
import pandas
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

data = pandas.read_csv("data/heartdisease/dataclean.csv")
y = data.num
x = data.drop("num",1)

model = lm.LinearRegression()
model.fit(x, y)
print(model.intercept_, model.coef_)


