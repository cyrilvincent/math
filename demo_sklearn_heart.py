import sklearn
import sklearn.linear_model as lm
import sklearn.neighbors as nn
import pandas as pd
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.preprocessing as preprocess
import numpy as np

np.random.seed(0)

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", axis=1)



xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, test_size=0.2, train_size=0.8)
# JAMAIS de fit sur xtest

scaler = preprocess.RobustScaler()
scaler.fit(xtrain)
xtrain = scaler.transform(xtrain) # lambda x: (x - mean) / std
xtest = scaler.transform(xtest)

# np.median(xtrain)
# np.quantile(xtrain, [0.25, 0.75])

# model = lm.LinearRegression()
model = nn.KNeighborsClassifier(n_neighbors=3)
# model = pipe.make_pipeline(pp.PolynomialFeatures(5), lm.Ridge())
model.fit(xtrain, ytrain)
predicted = model.predict(x)
# print(model.coef_, model.intercept_)

score_train = model.score(xtrain, ytrain)
score_test = model.score(xtest, ytest)
print(f"Score: {score_train} {score_test}")
