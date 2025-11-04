# pip install pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("data/mug.jpg")
array = np.asarray(im).astype(np.float64)
print(array.shape)

red = array[:,:,0]

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")

plt.imshow(red, cmap="Greys_r")
plt.show()

# Faire une fonction get_chanel(array, num) et qui me retourne la matrice du chanel, par exemple get_chanel(array, 0) -> red
# Créer les fonctions load & save qui charge et sauvegarde l'image
# Créer la fonction crop(array, north, south, east, west) crop(10,10,10,10) -> slice
# Créer la fonction reduce(array, nb), par exemple reduce(array, 2) -> ca me divise la taille l'image par 4
# Bonus créer la fonction superpose(array1, array2)
