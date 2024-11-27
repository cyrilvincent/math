import pandas as pd
import sklearn.neighbors as nn
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import sklearn.neighbors as nn
import numpy as np

df = pd.read_csv("data/breast-cancer/data.csv", index_col="id")
y = df.diagnosis
x = df.drop("diagnosis", axis=1)

scaler = pp.RobustScaler()
scaler.fit(x)
xscaled = scaler.transform(x)


np.random.seed(42)
xtrain, xtest,ytrain,ytest = ms.train_test_split(xscaled, y, train_size=0.8, test_size=0.2)

model = nn.KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain, ytrain)

score = model.score(xtest, ytest)
print(score)

xpredict = np.array([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])
xscaled = scaler.transform(xpredict)
print(xscaled)
predicted = model.predict(xscaled)
print(predicted)