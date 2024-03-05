import numpy as np
import pandas as pd

df = pd.read_csv("data/mesures/mesures.csv")
vt = df.VT.values
vm = df.VM.values
t = df["T"].values
np.savez("data/mesures/mesures.npz", vt=vt, vm=vm, t=t)

dict = np.load("data/mesures/mesures.npz")
vt = dict["vt"]
vm = dict["vm"]
t = dict["t"]
mat = np.array([t, vm, vt]).T
print(mat)
diff = mat[:,1]-mat[:,2]
print(mat[diff != 0])


