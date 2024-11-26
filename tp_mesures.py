import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pip install openpyxl

# df = pd.read_excel("data/mesures/mesures.xlsx", index_col="T")
df = pd.read_csv("data/mesures/mesures.csv", index_col="T")
df = df[df.index < 200]

plt.subplot(211)
plt.plot(df.VT)
plt.plot(df.VM, color="red")


diff = np.abs(df.VT - df.VM)
plt.subplot(212)
plt.plot(diff)
plt.show()

errors = df[np.abs(diff) > 0.01]
print(errors)

# Afficher VT et VM
# diff = |VT - VM|
# Afficher diff

