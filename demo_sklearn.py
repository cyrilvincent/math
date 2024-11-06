import pandas as pd
import numpy as np
import sklearn.linear_model as lm
import sklearn.ensemble as rf
import matplotlib.pyplot as plt
import sklearn.neural_network as neural

df = pd.read_csv("data/breast-cancer/data.csv", index_col="id")
y = df.diagnosis
x = df.drop("diagnosis", axis=1)

# model = lm.LinearRegression()
# model = rf.RandomForestClassifier(n_estimators=1000)
model = neural.MLPClassifier(hidden_layer_sizes=(30,30,30))  # Multi Layer Perceptron
model.fit(x, y)

data = np.array([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])
predicted = model.predict(data)
print(f"Predicted: {predicted}")
score = model.score(x, y)
print(score)

# print(model.feature_importances_)
# plt.bar(x.columns, model.feature_importances_)
# plt.xticks(rotation=45)
# plt.show()

# from sklearn.tree import export_graphviz
# export_graphviz(model.estimators_[0], out_file="data/breast-cancer/tree.dot", feature_names=x.columns,
#                 class_names=["0", "1"]
#                 )