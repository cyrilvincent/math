import pandas as pd
import numpy as np
import sklearn.linear_model as lm
import sklearn.ensemble as rf
import matplotlib.pyplot as plt

df = pd.read_csv("data/breast-cancer/data.csv", index_col="id")
y = df.diagnosis
x = df.drop("diagnosis", axis=1)

# model = lm.LinearRegression()
model = rf.RandomForestClassifier(n_estimators=1000)
model.fit(x, y)

predicted = model.predict(x)
score = model.score(x, y)
print(score)

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()

from sklearn.tree import export_graphviz
export_graphviz(model.estimators_[0], out_file="data/breast-cancer/tree.dot", feature_names=x.columns,
                class_names=["0", "1"]
                )