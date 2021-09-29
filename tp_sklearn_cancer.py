# Charger avec Pandas heartdisease
# y = num
# x le dataframe tout sauf num
# Fit les polynomes de degrés 1 à 10
# Bonus : idem cancer
# Critiquer le résultat pour un degrés de polynome important

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import sklearn.neural_network as nn
import sklearn.preprocessing as preprocess
import sklearn.pipeline as pipe
import sklearn.preprocessing as pp
import sklearn.neighbors as nn
import sklearn.ensemble as rf


dataframe = pd.read_csv("data/breast-cancer/data.csv",index_col="id",na_values=".")
y = dataframe.diagnosis
x = dataframe.drop("diagnosis",1)

np.random.seed(1)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

# for i in range(1,4):
#model = pipe.make_pipeline(pp.PolynomialFeatures(i), lm.Ridge())
#model = nn.KNeighborsClassifier(n_neighbors=3)
model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
print(model.score(xtrain, ytrain))
print(model.score(xtest, ytest))
print(list(zip(x.columns.values,model.feature_importances_)))
plt.bar(range(len(model.feature_importances_)), model.feature_importances_)
plt.show()
print(x.columns.values[20:24])
print(x.columns.values[6:8])

import sklearn.tree as tree
tree.export_graphviz(model.estimators_[0],
                out_file='data/breast-cancer/tree.dot',
                feature_names = x.columns,
                class_names = ["0", "1"],
                rounded = True, proportion = False,
                precision = 2, filled = True)