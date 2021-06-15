# pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
print(cube)
print(cube.shape)
print(cube.dtype)

red = cube[10:-10:2,10:-10:3,0]
print(np.min(red), np.max(red), np.mean(red), np.std(red))
im2 = Image.fromarray(red[-1:0:-1,-1:0:-1]).convert("RGB")
im2.save("data/modified.jpg")



# Télécharger une image depuis internet => data
# Transformer l'image en np.array
# Obtenir la composante Bleue
# Obtenir le point le + lumineux le - lumineux et la moyenne = luminance
# Obtenir le contraste (écart type = np.std)
# Cropper, resizer, inverser ligne et colonne, inverser les lignes
# Essayer d'additionner 2 images
# Fusionner les 3 canaux de couleur

im1 = Image.open("data/ski.jpg")
cube1 = np.asarray(im1)


im2 = Image.open("data/ski2.jpg")
cube2 = np.asarray(im2)

dim0 = min(cube1.shape[0], cube2.shape[0])
dim1 = min(cube1.shape[1], cube2.shape[1])
print(dim0, dim1)
cube1 = cube1[:dim0,:dim1].astype(np.float64)
cube2 = cube2[:dim0,:dim1].astype(np.float64)
add = (cube1 + cube2) // 2
im2 = Image.fromarray(add.astype(np.uint8)).convert("RGB")
im2.save("data/modified.jpg")