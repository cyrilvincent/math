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


# x = 30 columns
# Scaler
# kNN
# Fit
# Predict
# Score
# Save
# Pour quel k on a la meilleur accuracy
# accuracy ?