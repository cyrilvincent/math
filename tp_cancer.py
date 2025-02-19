import pandas as pd
import sklearn.neighbors as nn
import numpy as np

np.random.seed(0)
df = pd.read_csv("data/breast-cancer/data.csv")
y = df.diagnosis
x = df.drop(["diagnosis", "id"], axis=1)

# x = 30 columns
# kNN
# Fit
# Predict
# Score
# Save
# Pour quel k on a la meilleur accuracy
# accuracy ?