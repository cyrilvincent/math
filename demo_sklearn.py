import sklearn.preprocessing as pp
import sklearn.neural_network as neural
import pandas as pd
import sklearn.model_selection as ms
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("data/breast-cancer/data.csv")
y = df["diagnosis"]
x = df.drop(["diagnosis", "id"], axis=1)

scaler = pp.StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

model = neural.MLPClassifier(hidden_layer_sizes=(30,30,30))
model.fit(xtrain, ytrain)
ypred = model.predict(xtest)
print(model.score(xtest, ytest))

x = np.array([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])
x = scaler.transform(x)
ypred = model.predict(x)
print(ypred)
