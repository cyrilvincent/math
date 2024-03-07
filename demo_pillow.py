from PIL import Image
import numpy as np
# pip install Pillow

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)

print(array.shape)

crop = array[100:-100,100:-100,:]

dest = Image.fromarray(crop.astype(np.uint8)).convert("RGB")
dest.show()
dest.save("data/ski2.jpg")

my_value = 256
my_value = np.clip(0,255,my_value)

# TP
# Bonus : Mettre OO
# crop(north, south, east, west) -> 
# transpose
# get_chanel(num = 0,1,2) #RGB En entrée cube => matrice
# dynamic => max - min
# reduct(n) : 1 pixel sur n
# change_lum(n) : Chaque pixel est augmenté de n (np.clip)
# Bonus add(array1, array2) : additionner 2 image (de même resolution)
# TP2
# Luminance = np.mean() 127.5
# Contrast = np.std() 63.75
# Bonus : Median et quartile et 3/4tile => mean ~= median, quartile ~= 255-3/4tile
# Autolum = matrice + (127.5 - luminance)
# Bonus : Auto-lum-contrast = ((matrice - luminance) / contrast) * 63.75 + 127.5
# Bonus : transformer une image couleur en n/b = np.mean(axis=2)
# Bonus : profile horizontal = np.mean(axis = 0)
