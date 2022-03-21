# pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im).astype("float")
im_red = cube[:,:,0]
print(cube.shape)
print(cube.dtype)
im = im_red.T
im2 = Image.fromarray(im.astype(np.uint8)).convert("RGB")
im2.save("data/modified.jpg")

# TP
# Obtenir les canaux RED, GREEN, BLUE
# Afficher la dynamique et la luminance des canaux : min, max, avg
# Inverser l'image par un axe horizontal
# Inverser l'image par un axe vertical
# Diminuer la luminance de 10 : np.clip(x,0,255)
# Cropper l'image (10,10,10,10)
# Créer un vrai image N&B : avg de la 3ème dimension
# Superposer 2 images /!\ les images n'ont pas la même résolution
# Calculer le contraste, autoconstraster l'image

