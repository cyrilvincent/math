import numpy as np
from PIL import Image # pip install Pillow

im = Image.open("d:/T23S0746.8_CC28-2825A_SD_EPI_SIP_API_11_11.tif")
array = np.asarray(im).astype(np.float64)
print(array.shape)

# array = array[::2,::2]
# array = array[:,:,0]


dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
dest.show()
# dest.save("data/modified.jpg")

# TP
# Tout faire dans des fonctions
# load
# save
# show
# transpose
# get_channel(0 ou 1 ou 2)
# crop(north, south, east, west)
# reduct(n) enlever 1 colonne et une ligne sur n
# change_lum(delta) np.clip(x,0,255)
# change_lambda(l) : pour test 1.1*x-2
# Bonus : add(im1, im2) : add 2 images (de même resolution)

