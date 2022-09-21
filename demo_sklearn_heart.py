import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("data/heartdisease/dataclean.csv")

y = dataframe.num
x = dataframe.drop("num", axis=1)

model = lm.LinearRegression()
model.fit(x, y)

predicted = model.predict(x)
print(model.score(x, y))

print(model.coef_, model.intercept_)



