import numpy as np

data = np.load("data/house/house.npz")
print(data)
surfaces = data["np_surfaces"]
loyers = data["np_loyers"]

print(loyers, np.min(loyers), np.max(loyers))

loyers_per_m2 = loyers / surfaces
print(np.min(loyers_per_m2), np.max(loyers_per_m2), np.mean(loyers_per_m2))

loyers_predicted = 30.66 * surfaces

mse = np.mean((loyers_predicted - loyers) ** 2)
print(np.sqrt(mse))