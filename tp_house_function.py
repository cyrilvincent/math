import matplotlib.pyplot as plt
import numpy as np

def load(path):
    """
    Load the npz file
    :param path: the path
    :return: surface & loyer
    """
    dict = np.load(path)
    surface = dict["np_surfaces"]
    loyer = dict["np_loyers"]
    return surface, loyer

def display(x, y, z):
    """

    :param x:
    :param y:
    :param z:
    :return:
    """
    plt.subplot(211)
    plt.scatter(x, y)
    plt.subplot(212)
    plt.scatter(x, z)
    plt.show()

def stats(x):
    return np.min(x), np.max(x)

def filter(x, y, z, filter):
    return x[filter], y[filter], z[filter]

surface, loyer = load("data/house/house.npz")
print(surface.shape, loyer.shape)
loyer_per_m2 = loyer / surface
print(stats(surface))
display(surface, loyer, loyer_per_m2)
filtre = surface < 200
filter(surface, loyer, loyer_per_m2, filtre)
