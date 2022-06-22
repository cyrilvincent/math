import sklearn
import sklearn.linear_model as lm
import sklearn.neighbors as nn
import pandas as pd
import numpy as np
import sklearn.preprocessing as preprocess
import numpy as np
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import sklearn.tree as tree
import matplotlib.pyplot as plt

np.random.seed(0)

dataframe = pd.read_csv("data/breast-cancer/data.csv")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis", "id"], axis=1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

scaler = preprocess.RobustScaler()
scaler.fit(xtrain)
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

# model = nn.KNeighborsClassifier(n_neighbors=3)
model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
predicted = model.predict(xtest)

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()

tree.export_graphviz(model.estimators_[0], out_file="data/breast-cancer/tree.dot", feature_names=x.columns,
                     class_names=["0", "1"], filled=True)

score = model.score(xtest, ytest)
print(f"Score: {score}")
