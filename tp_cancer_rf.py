import pandas as pd
import sklearn.ensemble as rf
import numpy as np
import sklearn.preprocessing as pp
import matplotlib.pyplot as plt

np.random.seed(0)
df = pd.read_csv("data/breast-cancer/data.csv")
df["random"] = np.random.rand()
y = df.diagnosis
x = df.drop(["diagnosis", "id"], axis=1)
columns = x.columns

scaler = pp.RobustScaler()
scaler.fit(x)
x = scaler.transform(x)

model = rf.RandomForestClassifier()

model.fit(x, y)

ypred = model.predict(x)

features = model.feature_importances_
plt.bar(columns, features)
plt.xticks(rotation=45)
plt.show()

score = model.score(x, y)
print(score)

from sklearn.tree import export_graphviz
export_graphviz(model.estimators_[0], out_file="data/breast-cancer/out.dot", feature_names=x.columns, class_names=["0", "1"])


# x = 30 columns
# Scaler
# kNN
# Fit
# Predict
# Score
# Save
# Pour quel k on a la meilleur accuracy
# accuracy ?