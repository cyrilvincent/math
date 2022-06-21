# pip install Pillow
from PIL import Image
import numpy as np

im1 = Image.open("data/ski.jpg")
array1 = np.asarray(im1)
print(array1.shape)

red = array1[:,:,0].astype(float)
lum = np.mean(red)
print(lum)
contrast = np.std(red)
print(contrast)
min = np.min(red)
max = np.max(red)
print(min, max)

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/output.png")