import numpy as np
from PIL import Image # pip install Pillow

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



# open(path)
# save(array, path)
# get_chanel(array, 0) => red
# crop(array, top, bottom, left, right)
# sub_sampling(array, 2,2) si j'ai 1000x500 => 500x250
# negative(array)
# flip(array, horizontal=True)
if __name__ == '__main__':
    array = open("data/ski.jpg")
    red = get_chanel(array, 0)
    cropped = crop(red, 50,100,150,200)
    reduce = sub_sampling(array,2,2)
    save(reduce, "data/out.png")