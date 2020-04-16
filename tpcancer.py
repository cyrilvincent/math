# Charger avec pandas data/breast-cancer/data.csv
# Effacer la colonne id
# y = colonne diagnosis
# x = autres colonnes (30)
# Calculer un knn sur le dataset avec k = 3, 5, 7, ...
# Afficher score
# Afficher les prédictions

import pandas as pd
import sklearn.neighbors as nn
import sklearn.ensemble as rf

data = pd.read_csv("data/breast-cancer/data.csv")
data = data.drop("id", 1)
y = data['diagnosis']
x = data.drop("diagnosis", 1)
print(x.shape)
#model = nn.KNeighborsClassifier(n_neighbors=3)
model = rf.RandomForestClassifier()
model.fit(x, y)
print(model.score(x,y))
print((model.predict(x) - y).values)