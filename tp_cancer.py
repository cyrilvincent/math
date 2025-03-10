import pandas as pd
import sklearn.neighbors as nn
import numpy as np
import sklearn.preprocessing as pp

np.random.seed(0)
df = pd.read_csv("data/breast-cancer/data.csv")
y = df.diagnosis
x = df.drop(["diagnosis", "id"], axis=1)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
print(df.corr())


scaler = pp.RobustScaler()
scaler.fit(x)
x = scaler.transform(x)

model = nn.KNeighborsClassifier(n_neighbors=3)

model.fit(x, y)

ypred = model.predict(x)

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