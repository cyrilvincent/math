# pip install pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, num):
    return array[:,:,num]

def show(array):
    plt.imshow(array.astype(np.uint8), cmap="Greys_r")
    plt.show()

def crop(array, north, south, east, west):
    return array[north:-south,west:-east]

def reduce(array, factor):
    return array[::factor,::factor]

def flip(array):
    return array[::-1]

def superpose(a1, a2):
    return (a1 + a2) / 2

def luminance(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def black_and_white(array):
    return np.mean(array, axis=2)

def negative(array):
    return 255 - array

def row_profile(array):
    return np.mean(array, axis=0)

def col_profile(array):
    return np.mean(array, axis=1)

def norm(array):
    return np.clip(((array - luminance(array)) / contrast(array)) * 255/4 + 255/2, 0, 255)


if __name__ == '__main__':
    array = load("data/ski.jpg")
    n = norm(array)
    show(n)
    red = get_chanel(array, 0)
    cropped = crop(red,100,50,200,50)
    reduced = reduce(red,2)
    flipped = flip(red)
    superposed = superpose(red, flipped)
    print(luminance(array), contrast(array))
    nb = black_and_white(array)
    neg = negative(nb)
    array = load("data/rond_blanc.jpg")
    rprofile = row_profile(array)
    plt.subplot(211)
    plt.plot(rprofile)
    save(array, "data/out.png")
    plt.subplot(212)
    show(array)


# luminance
# black_white
# contrast : std
# bonus : negative
# horizontal_profile + vertical_profile
# bonus : normalize : ((x - lum) / contrast) * 255/4 + 255/2 + np.clip(mat,0,255)
