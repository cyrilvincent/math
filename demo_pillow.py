from PIL import Image
import numpy as np

def load(path):
    im = Image.open(path)
    array =  np.asarray(im).astype(float)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

array = load("data/ski.jpg")
red=array[:,:,0].T
save(red, "data/result.jpg")

# Afficher les canaux R, V, B
# Stats : lunimance : mean, par canaux ?
#   Min, Max
#   Contraste : std
# Modifier la luminance d'une image +lum np.clip(x,0,255)
# Crop(x) : Enlever x lignes et colonnes autour de l'image
# Convert B&W
# Autocontrast (Bonus)