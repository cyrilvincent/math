import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/mesures/mesures.csv") # pip install openpyxl
# Afficher dans matplotlib VT et VM
# Zoomer sur les différences
# diff = |VT-VM|
# Afficher diff
diff = np.abs(dataframe["VM"] - dataframe["VT"])
plt.subplot(211)
plt.scatter(dataframe["T"], dataframe["VM"])
plt.plot(dataframe["T"], dataframe["VT"], color="red")
plt.subplot(212)
plt.plot(dataframe["T"], diff)
plt.show()


