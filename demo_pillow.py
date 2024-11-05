import numpy as np
from PIL import Image # pip install pillow

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape) # RGB

red = array[:,:,0]
red = red[:,640:]
print(red.shape)

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
# dest.show()
dest.save("data/out.jpg")