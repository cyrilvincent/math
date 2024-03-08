# pip install scikit-learn
import sklearn.linear_model as lm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")

y = dataframe.num
x = dataframe.drop("num", axis=1)
print(x.values.shape)

model = lm.LinearRegression()

model.fit(x, y)

predicted = model.predict(x)
predicted = np.int32(np.abs(np.round(predicted)))

print(predicted)
errors = np.abs(predicted - y.values)
print(errors)
accuracy = len(errors[errors == 0]) / len(y)
print(accuracy)
print(model.coef_, model.intercept_)