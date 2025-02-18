import numpy as np
from PIL import Image # pip install pillow

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape, array.dtype)

red = array[:,:,0]
print(red.shape)
red = red.T

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")

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