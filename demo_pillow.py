# pip install Pillow
from PIL import Image
import numpy as np

def load(path):
    im = Image.open(path)
    return np.asarray(im).astype(float)

def get_canal(array, num):
    if 0 <= num <= 2:
        return array[:,:,num]
    else:
        raise ValueError("Bad num")

def stats(array):
    return np.min(array), np.max(array), np.mean(array), np.std(array)

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def change_lum(array, delta):
    return np.clip(array + delta, 0, 255)

def crop(array, nbcrop):
    return array[nbcrop: -nbcrop - 1, nbcrop: -nbcrop - 1]

def convert_bw(array3d):
    return np.mean(array3d, axis=2)

def autocontrast(array, delta):
    _,_, avg, std = stats(array)
    norm_array = (array - avg) / std
    return norm_array * 63.75 + 127.5

array = load("data/ski.jpg")
print(array.shape)
red = get_canal(array, 0)
min, max, mean, std = stats(array)
print(min, max, mean, std)
redt = red.T
_, _, mean, std = stats(red)
array_autolum = change_lum(red, 127.5 - mean)
save(array_autolum, "data/autolum.jpg")
array_crop = crop(red, 100)
save(array_crop, "data/crop.jpg")



