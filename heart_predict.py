import pickle
import numpy as np

with open("data/heartdisease/lm.pickle", "rb") as f:
    model = pickle.load(f)

x = np.array([[28,1,2,130,132,0,2,185,0,0]])
ypred = model.predict(x)
print(ypred)