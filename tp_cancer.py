import sklearn
import sklearn.linear_model as lm
import sklearn.neighbors as nn
import pandas as pd
import numpy as np

np.random.seed(0)

dataframe = pd.read_csv("data/breast-cancer/data.csv")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis", "id"], axis=1)

model = nn.KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)
predicted = model.predict(x)

score = model.score(x, y)
print(f"Score: {score}")
