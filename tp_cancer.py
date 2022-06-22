import sklearn
import sklearn.linear_model as lm
import sklearn.neighbors as nn
import pandas as pd
import numpy as np
import sklearn.preprocessing as preprocess
import numpy as np
import sklearn.model_selection as ms

np.random.seed(0)

dataframe = pd.read_csv("data/breast-cancer/data.csv")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis", "id"], axis=1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

scaler = preprocess.RobustScaler()
scaler.fit(xtrain)
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

model = nn.KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain, ytrain)
predicted = model.predict(xtest)

score = model.score(xtest, ytest)
print(f"Score: {score}")
