# pip install pillow
from PIL import Image
import numpy as np

im = Image.open("data/ski.jpg")
array = np.asarray(im).astype(np.float64)

print(array.shape)

red = array[:,500:,0]
print(red.shape)
print(red)

dest = Image.fromarray(red.astype(np.uint8)).convert("RGB")
dest.save("data/out.png")

# Obtenir les canaux red, green ou blue
# Faire la fonction crop(north, south, east, west)
# Reduce avec un entier reduce(img, 2) -> diminue l'image de'un facteur 4
# Augmenter la luminosite d'une image de 10%
# np.clip