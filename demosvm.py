import pandas

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
y = data.diagnosis
x = data.drop("diagnosis", 1)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y)

import sklearn.svm as svm
model = svm.SVC(C=0.1, kernel= "rbf")
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(score)