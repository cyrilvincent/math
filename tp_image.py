# pip install pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def get_chanel(array, num):
    return array[:, :, num]

def crop(array, north, south, east, west):
    return array[north:-south, west:-east]

def reduce(array, factor):
    n = int(np.sqrt(factor))
    return array[::n, ::n]

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def flip(array):
    return array[::-1]

def luminance(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def grayscale(array):
    return np.mean(array, axis=2)

def negative(array):
    return 255 - array

def profile_h(array):
    return np.mean(array, axis=0)

def profile_v(array):
    return np.mean(array, axis=1)

def normalize(array):
    return np.clip(((array - np.mean(array)) / np.std(array)) * 255/4 + 127.5, 0, 255)

array = load("data/ski.jpg")
print(luminance(array), contrast(array))
print(array.shape)
red = get_chanel(array, 0)
cropped = crop(red, 20, 40, 80 ,120)
reduced = flip(reduce(array, 4))
gray = grayscale(array)
neg = negative(array)
profh = profile_h(gray)
norm = normalize(array)
plt.plot(profh)
plt.show()
save(norm, "data/out.png")

# crop(array, north, south, east, west)
# luminance : mean
# contrast : std
# reduce(array, factor) => si factor=4 alors ca reduit l'image en 2 x 2
# flip : le chat a les pattes en haut
# grayscale : monochrome
# negative
# row_profile du grayscale => matplotlib
# col_profile => matplotlib
# Bonus : normaliser l'image = np.clip(((x - mean) / std) * 255/4 + 127.5, 0, 255)