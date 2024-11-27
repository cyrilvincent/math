import pandas as pd
import sklearn.neighbors as nn
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import sklearn.ensemble as rf
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = df.num
x = df.drop("num", axis=1)
x["rnd"] = np.random.rand(len(df))

scaler = pp.RobustScaler()
scaler.fit(x)
xscaled = scaler.transform(x)


np.random.seed(42)
xtrain, xtest,ytrain,ytest = ms.train_test_split(xscaled, y, train_size=0.8, test_size=0.2)

# model = nn.KNeighborsClassifier(n_neighbors=3)
model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

from sklearn.tree import export_graphviz

export_graphviz(model.estimators_[0], out_file="data/heartdisease/out.dot", feature_names=x.columns, class_names=["0", "1"])

