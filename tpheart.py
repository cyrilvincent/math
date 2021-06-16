import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn.neighbors as nn
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import matplotlib.pyplot as plt
import sklearn.tree as tree


dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", 1)

benin_filter = y == 0
malin_filter = y == 1

print(x[benin_filter].chol.describe())
print(x[malin_filter].chol.describe())

print(x[benin_filter].sex.describe())
print(x[malin_filter].sex.describe())

slope, intercept, r_value, p_value, std_err = stats.linregress(x.age, x.chol)
print(slope, intercept, r_value)
f = lambda x: slope * x + intercept

# plt.scatter(x.age, x.chol)
# plt.plot(np.arange(28,66), f(np.arange(28,66)))
# plt.show()

np.random.seed(0)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
plt.bar(x.columns, model.feature_importances_)
plt.show()
print(model.score(xtest, ytest))

tree.export_graphviz(model.estimators_[0],
                out_file='data/heartdisease/tree.dot',
                feature_names = x.columns,
                class_names = ["0", "1"],
                rounded = True, proportion = False,
                precision = 2, filled = True)