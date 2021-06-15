# pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
print(cube)
print(cube.shape)
print(cube.dtype)

red = cube[10:-10:2,10:-10:3,0]
im2 = Image.fromarray(red).convert("RGB")
im2.save("data/modified.jpg")

# Télécharger une image depuis internet => data
# Transformer l'image en np.array
# Obtenir la composante Bleue
# Obtenir le point le + lumineux le - lumineux et la moyenne = luminance
# Obtenir le contraste (écart type = np.std)
# Cropper, resizer, inverser ligne et colonne, inverser les lignes
# Essayer d'additionner 2 images
# Fusionner les 3 canaux de couleur


