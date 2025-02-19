import sklearn.linear_model as lm # pip install scikit-learn
import pandas as pd
import pickle
import sklearn.neighbors as nn
import sklearn.preprocessing as pp

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe["num"]
x = dataframe.drop("num", axis=1)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
print(dataframe.corr())

scaler = pp.StandardScaler()
scaler.fit(x)
x = scaler.transform(x)
print(scaler.inverse_transform(x))

# model = lm.LinearRegression()
model = nn.KNeighborsClassifier(n_neighbors=3)

model.fit(x, y)

ypred = model.predict(x)

score = model.score(x, y)
print(score)

with open("data/heartdisease/knn.pickle", "wb") as f:
    pickle.dump(model, f)