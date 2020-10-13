from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
a = np.asarray(im)
print(a.shape)
a = a.mean(axis = 2)
print(a.shape)
print(np.max(a))