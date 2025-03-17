import numpy as np
from PIL import Image # pip install Pillow

im = Image.open("data/ski.jpg")
array = np.asarray(im)
print(array.shape, array.dtype)
array = array.astype(np.float64)
print(array.shape, array.dtype)

red = array[:,:,0]

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.jpg")

# open(path)
# save(array, path)
# get_chanel(array, 0) => red
# crop(array, top, bottom, left, right)
# sub_sampling(array, 2,2) si j'ai 1000x500 => 500x250
# negative(array)
# flip(array, horizontal=True)
if __name__ == '__main__':
    pass
    # tests