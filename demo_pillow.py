from PIL import Image
import numpy as np

im = Image.open("data/foret.jpg")
array =  np.asarray(im).astype(float)
print(array.shape)

green = array[:,300:-300,1]

dest = Image.fromarray(green.astype(np.uint8)).convert("RGB")
dest.save("data/foret_modified.jpg")
dest.show()

# TP
# Charger une image de votre choix
# Créer un module avec des fonctions :
#   load(path) -> np.array
#   save(path, array)
#   show(array) : affiche l'image à l'écran
#   crop(array, nb) -> array: crop nb ligne en EST, OUEST, NORD, SUD
#   get_chanel(array, num: int) -> 0 = RED, 1=GREEN, 2=BLUE
#   Tester toutes les fonctions en sauvegardant les images
#   add(array1, array2) -> additionne 2 images, de shape identique
#   Bonus : Si les 2 images sont de résolutions différentes autocropper la + grande vers la + petite