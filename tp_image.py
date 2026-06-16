# pip install pillow
from PIL import Image
import numpy as np

def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def get_chanel(array, num):
    return array[:, :, num]

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)


array = load("data/ski.jpg")
print(array.shape)
red = get_chanel(array, 0)
save(red, "data/out.png")

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