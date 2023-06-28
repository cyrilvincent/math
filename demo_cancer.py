import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.ensemble as rf
import sklearn.preprocessing as pp
import sklearn.neural_network as neural

dataframe = pd.read_csv("data/breast-cancer/data.csv", index_col="id")

y = dataframe.diagnosis
x = dataframe.drop("diagnosis", axis=1)
xoriginal = x

scaler = pp.RobustScaler()
scaler.fit(x, y)
x = scaler.transform(x)

# model = rf.RandomForestClassifier()
model = neural.MLPClassifier((30,30,30))
model.fit(x, y)

# print(model.feature_importances_)
# plt.bar(xoriginal.columns, model.feature_importances_)
# plt.xticks(rotation=45)
# plt.show()

predicted = model.predict(x)
print(x.shape)
print(model.score(x, y))

# print(model.coef_, model.intercept_)