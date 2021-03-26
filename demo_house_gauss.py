import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

dataframe = pandas.read_csv("data/house/house.csv")

loyerparm2 = dataframe.loyer / dataframe.surface
loyerparm2 = loyerparm2[dataframe.loyerparm2 < 50]

print(np.mean(loyerparm2), np.std(loyerparm2), np.min(loyerparm2), np.max(loyerparm2))

normtest = scipy.stats.normaltest(loyerparm2)
print(normtest)
# Seuils p > 0.01

min = 20
max = 82
pack = 1
gauss = []
for i in range((max + pack - min) // pack):
    gauss.append(0)

for v in loyerparm2.values:
    i = int((v - min) // pack)
    gauss[i] += 1

print(gauss)
plt.bar(range(len(gauss)), gauss)
plt.show()
