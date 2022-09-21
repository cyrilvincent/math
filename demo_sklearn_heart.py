import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.neighbors as nn
import sklearn.ensemble as rf

dataframe = pd.read_csv("data/heartdisease/dataclean.csv")

y = dataframe.num
x = dataframe.drop("num", axis=1)

# model = lm.LinearRegression()
# model = nn.KNeighborsClassifier(n_neighbors=3)
model = rf.RandomForestClassifier()
model.fit(x, y)

predicted = model.predict(x)
print(model.score(x, y))

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()




# print(model.coef_, model.intercept_)



