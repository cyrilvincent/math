import matplotlib.pyplot as plt
import numpy as np

dict = np.load("data/house/house.npz")
surface = dict["np_surfaces"]
loyer = dict["np_loyers"]
print(loyer)