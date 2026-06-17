import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("data/jena/jena_climate_2009_2016.csv")
y = data["T (degC)"][11::24 * 6]
x = np.arange(len(y))

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)

plt.title("Temp")
plt.plot(x, y, color="blue")
plt.plot(x, slope * x + intercept, color="red")
plt.show()

print(slope * 365)


