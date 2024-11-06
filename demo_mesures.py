import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np

df = pd.read_csv("data/mesures/mesures.csv")
df = df[df["T"] < 125]
x = df["T"]
y1 = df.VT
y2 = df.VM

plt.subplot(211)
plt.plot(x, y1)
plt.plot(x, y2, color="red")

errors = np.abs(y1-y2)
area = np.sum(errors)
print(area / 125)

plt.subplot(212)
plt.plot(x, errors)
plt.show()

# area = integrate.quad(errors,0,125)
# print(area)