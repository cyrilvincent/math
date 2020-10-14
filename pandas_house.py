import pandas
import matplotlib.pyplot as plt
import sqlite3

#dataframe = pandas.read_csv("data/house/house.csv")
# with sqlite3.connect("data/house/house.db3") as conn:
#     dataframe = pandas.read_sql("select loyer, surface from house", conn)
dataframe = pandas.read_excel("data/house/house.xlsx")
surfaces = dataframe.surface
loyers = dataframe.loyer

plt.scatter(surfaces, loyers)
plt.show()