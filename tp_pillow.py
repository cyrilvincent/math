import numpy as np
from PIL import Image # pip install Pillow
import matplotlib.pyplot as plt
import my_library

def open(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, num):
    return array[:,:,num]

def crop(array, top, bottom, left, right):
    return array[top:-bottom, left:-right]

def sub_sampling(array, row, col):
    return array[::row, ::col]

def negative(array):
    return np.abs(array - 255)

def flip(array, horizontal=True):
    if horizontal:
        return array[::-1]
    else:
        return array[:, ::-1]

def luminance(array):
    return np.mean(array)

def luminance3(array):
    return np.mean(get_chanel(array, 0)), np.mean(get_chanel(array, 1)), np.mean(get_chanel(array, 2))

def contrast(array):
    return np.std(array)

def profile(array, horizontal=True):
    if horizontal:
        return np.mean(array, axis=0)
    else:
        return np.mean(array, axis=1)

def black_white(array):
    return np.mean(array, axis=2)

def auto_lum_contrast(array, sigmoid=True):
    norm = (array - luminance(array)) / contrast(array)
    denorm = norm * 255/4 + 127.5
    if not sigmoid:
        return np.clip(denorm, 0, 255)
    else:
        return my_library.sigmoid(denorm / 255) * 255


# open(path)
# save(array, path)
# get_chanel(array, 0) => red
# crop(array, top, bottom, left, right)
# sub_sampling(array, 2,2) si j'ai 1000x500 => 500x250
# negative(array)
# flip(array, horizontal=True)
# luminance = mean = 127.5
# contraste = std = 255/4
# profil(horizontal=True)
# black_white =
# auto_lum_contrast = ((x - mean) / std) * 255/4 + 127.5 : sans clip, puis avec np.clip puis avec sigmoid
if __name__ == '__main__':
    array = open("data/ski.jpg")
    red = get_chanel(array, 0)
    cropped = crop(red, 50,100,150,200)
    reduce = sub_sampling(array,2,2)
    neg = negative(red)
    flipped = flip(array, horizontal=True)
    print(f"Luminance: {luminance(array)}, contrast: {contrast(array)}")
    print(f"Luminance3: {luminance3(array)}")
    profiled_h = profile(array, horizontal=True)
    profiled_v = profile(array, horizontal=False)
    bw = black_white(array)
    auto = auto_lum_contrast(array, sigmoid=True)
    save(auto, "data/out.png")
    plt.subplot(211)
    plt.plot(profiled_h)
    plt.subplot(212)
    plt.plot(profiled_v)
    plt.show()
