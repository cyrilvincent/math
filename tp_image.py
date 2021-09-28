# pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im)
print(cube.shape)

red = cube[:,:,0]
print(red.shape)
redt = red.T

im2 = Image.fromarray(redt).convert(("RGB"))
im2.save("data/modified.jpg")

# TP
# Telecharger 2 images
# Transformer l'image en np.array
# Prendre la composante verte => matrice
# Calculer la moyenne de la matrice (luminance), min, max
# Cropper la matrice : 1280x715 => 1000x700 enlevant les bords
# 3/2 => 1.5, 3//2 => 1
# Transposer la matrice
# Inverser les lignes
# Additionner 2 images
# Convertir l'image couleur en N/B => que un point est la moyenne des 3 niveau de couleur
#   R=100, V=110, B=120 => N/B = 110
# Bonus : resizer une image
# Bonus : np.std => contraste
# Bonus : augmenter ou baisser la luminosité d'une image de x %
# Bonus : Augmenter le contraste d'une image de x %

