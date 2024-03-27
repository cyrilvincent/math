import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.ensemble as en
import sklearn.model_selection as ms

np.random.seed(0)
dataframe= pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", axis=1)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y, test_size=0.2, train_size=0.8)

#model = lm.LinearRegression()
model = en.RandomForestClassifier()
model.fit(xtrain, ytrain)
print(model.score(xtrain, ytrain))
print(model.score(xtest, ytest))
predicted = model.predict(xtest)
print(predicted)

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()

from sklearn.tree import export_graphviz
export_graphviz(model.estimators_[0],
                 out_file='data/breast-cancer/tree.dot',
                 feature_names = x.columns,
                 class_names = ["0", "1"],
                 rounded = True, proportion = False,
                 precision = 2, filled = True)