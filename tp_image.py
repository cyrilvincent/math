from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape)

red = array[:,:,0]
red = red.T

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")

# Créer la fonction open(path)
# Créer la fonction save(path)
# get_chanel(nb)
# transpose
# crop(north, south, east, west)
# reduce(factor)

