from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
print(cube.ndim)
print(cube.shape)
red = cube[10:-10,10:-10,0]
nb = np.mean(cube, axis = 2)
print(np.std(cube))
im2 = Image.fromarray(nb).convert("RGB")
im2.save("data/modified.jpg")

# tp
# Télécharger une image depuis internet => data
# Transformer l'image en np.array
# Obtenir la composante bleu
# Obtenir le point le + lumineux et le - lumineux et la moyenne (luminance)
# Obtenir le contraste (ecart type)
# Essayer inverser ligne colonne des images
# Essayer d'additionner 2 images, savoir croper une image
# Sauver l'image
