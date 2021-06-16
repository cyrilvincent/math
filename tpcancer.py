import pandas as pd
import numpy as np
import sklearn.linear_model as lm

# Charger breast-cancer/data.csv avec pandas read_csv(...,index_col="id")
# y = dataframe["diagnosis"] 0=benin 1 = malin
# x = dataframe.drop("diagnosis",1).drop("id")

# Sur x
# Chercher 2 colonnes qui gère la taille et la concavité
# Calculer sur ces 2 colonnes min,max,mean,std,median,quantile
# Retenez la valeurs mean et std
# Trouver une correlation
# x_benin = 0
# x_malin = 1

dataframe = pd.read_csv("data/breast-cancer/data.csv", index_col="id")
print(dataframe)
y = dataframe.diagnosis
x = dataframe.drop("diagnosis", 1)

benin_filter = y == 0
malin_filter = y == 1

print(x[benin_filter].radius_mean.describe())
print(x[malin_filter].radius_mean.describe())

print(x[benin_filter].concave_points_mean.describe())
print(x[malin_filter].concave_points_mean.describe())

model = lm.LinearRegression()
model.fit(x, y)
print(model.coef_, model.intercept_)
print(model.score(x, y))