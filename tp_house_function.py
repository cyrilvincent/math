import matplotlib.pyplot as plt
import numpy as np

def load(path):
    dict = np.load(path)
    print(dict.keys())
    surface = dict["np_surfaces"]
    loyer = dict["np_loyers"]
    return surface, loyer

if __name__ == '__main__':
    surface, loyer = load("data/house/house.npz")
    print(surface.shape, loyer.shape)