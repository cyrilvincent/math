import numpy as np
import pandas
import sklearn.linear_model as lm
import sklearn.neighbors as neighbors
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.ensemble as rf
import sklearn.neural_network as nn
import sklearn.preprocessing as preprocess

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
y = data.diagnosis
x = data.drop("diagnosis", 1)

np.random.seed(0)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

# model = neighbors.KNeighborsClassifier(n_neighbors=3)
# model = rf.RandomForestClassifier(n_estimators=100)
model = nn.MLPClassifier(hidden_layer_sizes=(30,20))
# nb_hidden_layer ~= log(len(data))
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))
print((model.predict(xtest) - ytest).values)

# print(list(zip(data.columns.values, model.feature_importances_)))

# plt.bar(range(len(model.feature_importances_)), model.feature_importances_)
# plt.show()