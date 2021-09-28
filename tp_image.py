# pip install Pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
cube = np.asarray(im).astype("float")
print(cube.shape)
print(cube.dtype)

red = cube[:,:,0]
print(red.shape)
redt = red.T
print("Moyenne:", np.mean(red), np.min(red), np.max(red))

crop = red[100:-100, 100:-100]
inverse = red[-1:0:-1]
inverse2 = red[:,-1:0:-1]

crop = red[:576,:1024]
im2 = Image.open("data/ski2.jpg")
array2 = np.asarray(im2).astype("float")
red2 = array2[:,:,0]
add = (crop + red2) / 2

nb = cube.mean(axis=2)
print(nb.shape)

contrast = cube.std()
print("Contraste:", contrast)

cubeminus10 = np.clip(cube * 0.9,0,255)

cubeautocontrast = np.clip(cube * (64 / np.std(cube)),0,255)

im2 = Image.fromarray(cubeautocontrast.astype(np.uint8)).convert("RGB")
im2.save("data/modified.jpg")



#  plt.imshow(matrice,cmap=plt.cm.gray_r,interpolation="nearest")

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

