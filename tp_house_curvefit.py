import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()
# Curvefiter une courbe en U (polynome de degré 2 puis 3)