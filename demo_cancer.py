import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp
import sklearn.model_selection as ms
import sklearn.neighbors as nn
import sklearn.ensemble as rf
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import sklearn.neural_network as neural
import pickle

dataframe = pd.read_csv("data/breast-cancer/data.csv")
print(dataframe["perimeter_worst"].describe())
dataframe.to_html("data/breast-cancer/data.html")

y = dataframe.diagnosis
x = dataframe.drop(["diagnosis", "id"], axis=1)

# scaler = pp.StandardScaler()
# scaler.fit(x)
# x = scaler.transform(x)

np.random.seed(0)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

scaler = pp.StandardScaler()
scaler.fit(x)
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
ypredicted = model.predict(xtest)

score = model.score(xtest, ytest)
print(f"Score: {score:.2f}")

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()






# print(x["perimeter_mean"])
# mean = np.mean(x["perimeter_mean"])
# std = np.std(x["perimeter_mean"])
# print(f"Mean: {mean}, std:{std}")
# norm = (x["perimeter_mean"] - mean) / std
# print(norm)
#
# print(x["smoothness_se"])
# mean = np.mean(x["smoothness_se"])
# std = np.std(x["smoothness_se"])
# print(f"Mean: {mean}, std:{std}")
# norm = (x["smoothness_se"] - mean) / std
# print(norm)



