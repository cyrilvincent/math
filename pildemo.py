from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
# print(cube.ndim)
# print(cube.shape)
red = cube[10:-10,10:-10,0]
blue = cube[:,:,2]
# print(np.min(blue), np.max(blue), np.mean(blue), np.std(blue))
inverse = blue.T
# nb = np.mean(cube, axis = 2)
# print(np.std(cube))
im2 = Image.fromarray(inverse).convert("RGB")
im2.save("data/modified.jpg")


im1 = Image.open("data/ski.jpg")
cube1 = np.asarray(im1)
print(cube1.shape)

im2 = Image.open("data/ski2.jpg")
cube2 = np.asarray(im2)
print(cube2.shape)
difx = cube1.shape[0] - cube2.shape[0]
dify = cube1.shape[1] - cube2.shape[1]
cube1 = cube1[difx // 2:-difx // 2, dify // 2:-dify // 2]
print(cube1.shape, cube2.shape)
cube_res = (cube1 + cube2) // 2
im2 = Image.fromarray(cube_res)
im2.save("data/merged.jpg")



# tp
# Télécharger une image depuis internet => data
# Transformer l'image en np.array
# Obtenir la composante bleu
# Obtenir le point le + lumineux et le - lumineux et la moyenne (luminance)
# Obtenir le contraste (ecart type)
# Essayer inverser ligne colonne des images
# Essayer d'additionner 2 images, savoir croper une image
# Sauver l'image
