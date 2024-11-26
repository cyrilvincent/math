from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def open(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, num):
    return array[:,:,num]

def transpose(array):
    return np.transpose(array, (1, 0, 2))

def crop(array, north, south, east, west):
    return array[north:array.shape[0]-south, east:-west]

def reduce(array, factor):
    return array[::factor, ::factor]

def luminance(array):
    return np.mean(array)

def contrast(array):
    return np.std(array)

def black_white(array):
    return np.mean(array, axis=2)

def vertical_profile(array):
    array = black_white(array)
    return np.mean(array, axis=1)



if __name__ == '__main__':
    array = open("data/ski.jpg")
    print(f"Luminance: {luminance(array):.2f}")
    print(f"Contrast: {contrast(array):.2f}")
    red = get_chanel(array, 0)
    arrayt = transpose(array)
    cropped = crop(array,50,100, 150,200)
    reduced = reduce(array, 2)
    bw = black_white(array)
    save(bw,"data/out.png")

    array2 = open("data/rond_blanc.jpg")
    profiled = vertical_profile(array2)
    plt.bar(np.arange(len(profiled)), profiled)
    plt.show()



