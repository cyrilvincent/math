import pandas as pd
import sklearn.linear_model as sklm
import matplotlib.pyplot as plt
import numpy as np
import sklearn.neighbors as nn
import sklearn.ensemble as rf

data = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = data['num']
x = data.drop("num", 1)

#model = nn.KNeighborsClassifier(n_neighbors=3)
model = rf.RandomForestClassifier()
model.fit(x, y)
print(model.score(x,y))
print(model.predict(x))