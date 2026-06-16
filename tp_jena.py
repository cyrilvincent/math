import numpy as np

data = np.load("data/jena/jena.npz")
print(data)
preasures = data["p"]
temps = data["t"]
x = np.arange(len(data))

# Afficher les temps el preasures dans un subplot
# Afficher une seul temperature par jour : donc prendre une temperature sur 24


