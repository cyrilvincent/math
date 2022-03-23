import pickle
import numpy as np

with open("data/breast-cancer/model.pickle", "rb") as f:
    model = pickle.load(f)

data = np.random.rand(30) * 2 - 1
predicted = model.predict(data.reshape(1, -1))
print(predicted)