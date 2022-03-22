# pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im).astype("float")
im_red = cube[:,:,0]
im_green = cube[:,:,1]
print(np.mean(im_red), np.min(im_red), np.max(im_red), np.std(im_red))
print(cube.shape)
print(cube.dtype)
# im = im_red.T

im_inverse = im_red[-1::-1]
im_inverse2 = im_red[:, -1::-1]

im_lum = np.clip(im_red * 1.2, 0, 255)

im_nb = np.mean(cube, axis=2)

im_crop = im_nb[100:-101, 100:-101]

im = Image.open("data/ski2.jpg")
cube2 = np.asarray(im).astype("float")

row_min = min(cube.shape[0], cube2.shape[0])
col_min = min(cube.shape[1], cube2.shape[1])
print(row_min, col_min)

cube_crop = cube[(cube.shape[0] - row_min) // 2 + 1 : -((cube.shape[0] -row_min) // 2) - 1, (cube.shape[1] - col_min) // 2 : -((cube.shape[1] - col_min) // 2) - 1]
cube2_crop = cube2[(cube2.shape[0] - row_min) // 2 : -((cube2.shape[0] - row_min) // 2) - 1, (cube2.shape[1] - col_min) // 2 : -((cube2.shape[1] - col_min) // 2) - 1]
print(cube_crop.shape, cube2_crop.shape)


cube_superpose = (cube_crop + cube2_crop) / 2

cubeautocontrast = np.clip(cube * (64 / np.std(cube)),0,255)

im2 = Image.fromarray(cube_superpose.astype(np.uint8)).convert("RGB")
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

