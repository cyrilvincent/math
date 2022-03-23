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

np.random.seed(1)
dataframe = pd.read_csv("data/breast-cancer/data.csv",index_col="id",na_values=".")
y = dataframe.diagnosis
x = dataframe.drop("diagnosis", axis=1)

scaler = preproc.RobustScaler()
scaler.fit(x)
x = scaler.transform(x)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

model = nn.KNeighborsClassifier(3)
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)

with open("data/breast-cancer/model.pickle", "wb") as f:
    pickle.dump(model, f)


