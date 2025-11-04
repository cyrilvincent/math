# pip install pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load(path):
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array, path):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array, num):
    return array[:,:,num]

def show(array):
    plt.imshow(array, cmap="Greys_r")
    plt.show()

def crop(array, north, south, east, west):
    return array[north:-south,west:-east]

def reduce(array, factor):
    return array[::factor,::factor]

def flip(array):
    return array[::-1]

def superpose(a1, a2):
    return (a1 + a2) / 2


if __name__ == '__main__':
    array = load("data/mug.jpg")
    red = get_chanel(array, 0)
    cropped = crop(red,100,50,200,50)
    reduced = reduce(red,2)
    flipped = flip(red)
    superposed = superpose(red, flipped)
    save(superposed, "data/out.png")
    show(superposed)


# Faire une fonction get_chanel(array, num) et qui me retourne la matrice du chanel, par exemple get_chanel(array, 0) -> red
# Créer les fonctions load & save qui charge et sauvegarde l'image
# Créer la fonction crop(array, north, south, east, west) crop(10,10,10,10) -> slice
# Créer la fonction reduce(array, nb), par exemple reduce(array, 2) -> ca me divise la taille l'image par 4
# Bonus créer la fonction superpose(array1, array2)
