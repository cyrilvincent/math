# pip install pillow
from PIL import Image
import numpy as np

def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, chanel):
    return array[:,:,chanel]

def crop(array, north, south, east, west):
    return array[north:-south,east:-west]

def lum(array, delta):
    return np.clip(array * delta, 0, 255)

def reduce(array, nb):
    return array[::nb,::nb]



# Obtenir les canaux red, green ou blue
# Faire la fonction crop(north, south, east, west)
# Reduce avec un entier reduce(img, 2) -> diminue l'image de'un facteur 4
# Augmenter la luminosite d'une image de 10%
# np.clip

if __name__ == '__main__':
    array = load("data/ski.jpg")
    print(array.shape)
    red = get_chanel(array, 0)
    croped = crop(red, 200,300,400,500)
    lum20 = lum(array, 1.2)
    reduce2 = reduce(array,2)
    save(reduce2, "data/out.jpg")