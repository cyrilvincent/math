from PIL import Image
import numpy as np

def open(path):
    im = Image.open("data/ski.jpg")
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


if __name__ == '__main__':
    array = open("data/ski.jpg")
    red = get_chanel(array, 0)
    arrayt = transpose(array)
    cropped = crop(array,50,100, 150,200)
    reduced = reduce(array, 2)
    save(reduced,"data/out.png")

