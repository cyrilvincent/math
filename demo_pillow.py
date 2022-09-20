from PIL import Image
import numpy as np

def load(path):
    im = Image.open(path)
    array =  np.asarray(im).astype(float)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def luminance(array):
    return np.mean(array)

array = load("data/foret.jpg")
red=array[:,:,0]
save(red, "data/result-red.jpg")
green=array[:,:,1]
save(green, "data/result-green.jpg")
blue=array[:,:,2]
save(blue, "data/result-blue.jpg")

lum_red = luminance(red)
print(lum_red)
lum_green = luminance(green)
print(lum_green)
lum_blue = luminance(blue)
print(lum_blue)

# Afficher les canaux R, V, B
# Stats : lunimance : mean, par canaux ?
#   Min, Max
#   Contraste : std
# Modifier la luminance d'une image +lum np.clip(x,0,255)
# Crop(x) : Enlever x lignes et colonnes autour de l'image
# Convert B&W
# Autocontrast (Bonus)