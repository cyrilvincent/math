import numpy as np
from PIL import Image # pip install pillow
import matplotlib.pyplot as plt

def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, nb):
    """
    Get the RGB chanel 0,1,2
    :param array: img 3d array
    :param nb: chanel nb must be 0,1,2
    :return: a matrix
    """
    return array[:,:,nb]

def crop(array, north, south, east, west):
    return array[north:-south,east:-west]

def reduce(array, nb_row, nb_col):
    return array[::nb_row, ::nb_col]

def lum(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def negative(array):
    return np.abs(array-255)

def bw(array):
    return np.mean(array, axis=2)

def horizontal_profile(array):
    return np.mean(array, axis=0)

def vertical_profile(array):
    return np.mean(array, axis=1)

def normalize(array):
    l = lum(array)
    c = contrast(array)
    centre_reduite = (array - l) / c
    return np.clip(centre_reduite * 255/4 + 255/2,0,255)


#
#
# red = array[:,:,0]
# print(red.shape)
# red = red.T
#
# dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
# dest.save("data/out.png")

# Obtenir le canal vert (get_chanel(num))
# Cropper l'image sur 100 pixels
# Facultatif : faire la fonction crop(north, south, east, west)
# Reduce : reduce(2,2) divise l'image par 4
# Lum
# Contrast : std
# Negative
# Black_white
# vetical_profile & horizontal_profile
# Bonus : autom_lum_contrast => lum=127.5, contrast = 63.75

if __name__ == '__main__':
    array = load("data/ski.jpg")
    print(array.shape)
    green = get_chanel(array, 1)
    cropped = crop(green, 50,100,150,200)
    result = reduce(green,2,2)
    bw = bw(array)
    result = negative(bw)
    print(f"Luminance: {lum(array):.2f}, Contrast:{contrast(array):.2f}")
    result = normalize(array)
    save(result, "data/out.png")

    # array = load("data/rond_blanc.jpg")
    profile = horizontal_profile(array)
    plt.plot(profile)
    plt.show()