from PIL import Image
# pip install pillow
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt

# Faire la fonction load
# Faire la fonction save
# get_chanel(array, num)
# crop(array, north, south, east, west)
# reduce(array, factor) => factor=2 ca reduit la taille de l'image par 4
# flip(array) => Le haut devienne la bas
# luminance
# contrast
# black_white
# negative
# row_profile => matplotlib
# column_profile => matplotlib
# bonus : norm


def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array


def save(array : NDArray[np.float64], path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)


def get_chanel(array, num):
    return array[:,:,num]


def crop(array, north, south, east, west):
    return array[north:-south, east:-west]


def reduce(array, factor: int):
    return array[::factor, ::factor]


def flip(array):
    return array[::-1]

def lum(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def black_white(array):
    return array.mean(axis=2)

def negative(array):
    return 255 - array

def profile(array, axis: int):
    return np.mean(array, axis=axis)

def norm(array):
    mean = lum(array)
    std = contrast(array)
    return np.clip(((array - mean) / std) * 255/4 + 255/2, 0, 255)


array = load("data/ski.jpg")
red = get_chanel(array, 0)

cropped = crop(red, 100, 200, 300, 400)
reduced = reduce(red, 2)
flipped = flip(reduced)
bw = black_white(array)
negative = negative(array)
row_profile = profile(array, 1)

norm_img = norm(array)
plt.plot(row_profile)
plt.show()
print(f"Lum: {lum(array)}, Contrast: {contrast(array)}")
save(norm_img, "data/out.png")
