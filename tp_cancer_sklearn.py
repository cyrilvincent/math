# Cancer
# y = diagnosis
# x = tout sauf dignosis, id
# train_test_split
# KNN avec k = 3, 5 7
# Fit avec train
# Score avec test
# Biais

import pandas as pd
import sklearn.model_selection as ms
import sklearn.neighbors as nn
import numpy as np
import sklearn.preprocessing as preproc
import pickle
import sklearn.ensemble as rf
import matplotlib.pyplot as plt
import sklearn.neural_network as nn

np.random.seed(1)
dataframe = pd.read_csv("data/breast-cancer/data.csv",index_col="id",na_values=".")
y = dataframe.diagnosis
xorig = dataframe.drop("diagnosis", axis=1)

scaler = preproc.RobustScaler()
scaler.fit(xorig)
x = scaler.transform(xorig)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

# model = nn.KNeighborsClassifier(3)
# model = rf.RandomForestClassifier()
model = nn.MLPClassifier((30,30,30))
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)

print(score)

with open("data/breast-cancer/model_nn.pickle", "wb") as f:
    pickle.dump(model, f)

# plt.bar(xorig.columns, model.feature_importances_)
# plt.xticks(rotation=45)
# plt.show()


