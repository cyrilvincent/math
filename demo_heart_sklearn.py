import pandas as pd
import sklearn.neighbors as nn
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import numpy as np

df = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = df.num
x = df.drop("num", axis=1)

scaler = pp.RobustScaler()
scaler.fit(x)
xscaled = scaler.transform(x)


np.random.seed(42)
xtrain, xtest,ytrain,ytest = ms.train_test_split(xscaled, y, train_size=0.8, test_size=0.2)

model = nn.KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

