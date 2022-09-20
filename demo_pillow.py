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

def stats(array):
    return np.mean(array), np.min(array), np.max(array), np.std(array)


def crop(array, nb):
    return array[nb:-nb, nb:-nb]

def convert_nb(array):
    return np.mean(array, axis=2)

def auto_lum_contrast(array):
    lum, min, max, std = stats(array)
    array_norm = (array - lum) / std
    return np.clip((array_norm * 63.75) + 127.5, 0, 255)

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

lum, min, max, std = stats(array)

print(min, max, std)

array_crop = crop(array, 50)
save(array_crop, "data/result-crop.jpg")

array_nb = convert_nb(array)
save(array_nb, "data/result_nb.jpg")

array_norm = auto_lum_contrast(array)
save(array_norm, "data/result_norm.jpg")

# Afficher les canaux R, V, B
# Stats : lunimance : mean, par canaux ?
#   Min, Max
#   Contraste : std
# Modifier la luminance d'une image +lum np.clip(x,0,255)
# Crop(x) : Enlever x lignes et colonnes autour de l'image
# Convert B&W
# Autocontrast (Bonus)