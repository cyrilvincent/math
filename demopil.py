#pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
print(cube.shape)
red = cube[:,:,0]
noiretblanc = np.mean(cube, axis = 2)
print(np.std(cube))
print(noiretblanc.shape)
print(np.max(noiretblanc))
print(np.mean(noiretblanc))

delta = np.mean(noiretblanc) - 127.5

norm = np.clip(0,255, noiretblanc - delta)

im = Image.fromarray(norm).convert('RGB')
im.save("data/modified.png")