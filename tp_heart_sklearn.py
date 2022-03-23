import pandas as pd
import sklearn.neighbors as nn
import sklearn.ensemble as rf
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heartdisease/data_with_nan.csv", na_values=".")
dataframe = dataframe.drop(["slope", "ca"], axis=1).drop("thal", axis=1)
dataframe = dataframe.dropna()

y = dataframe.num
x = dataframe.drop("num", axis=1)

# model = nn.KNeighborsClassifier(3)
model = rf.RandomForestClassifier()
model.fit(x, y)
score = model.score(x, y)
print(score)

print(list(zip(x.columns, model.feature_importances_)))

plt.bar(x.columns, model.feature_importances_)
plt.show()




