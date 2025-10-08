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

def get_chanel(array, chanel):
    return array[:,:,chanel]

def crop(array, north, south, east, west):
    return array[north:-south,east:-west]

def lum(array, delta):
    return np.clip(array * delta, 0, 255)

def reduce(array, nb):
    return array[::nb,::nb]

def get_luminance(array):
    return np.mean(array)

def get_contrast(array):
    return np.std(array)

def auto_normalize(array):
    mean = np.mean(array)
    std = np.std(array)
    return np.clip(((array - mean) / std) * (255 / 4) + 127.5,0,255)

def profil(array, axis):
    return np.mean(array, axis=axis)



# Obtenir les canaux red, green ou blue
# Faire la fonction crop(north, south, east, west)
# Reduce avec un entier reduce(img, 2) -> diminue l'image de'un facteur 4
# Augmenter la luminosite d'une image de 10%
# np.clip

# Calculer luminance et le contraste (mean, std)
# Calculer les 2 profils et l'afficher en matplotlib
# Bonus : Autonormaliser l'image => lum=255/2, contraste=255/4, ((pix - mean) / std) * 255 /4 + 255 / 2

if __name__ == '__main__':
    array = load("data/ski.jpg")
    print(array.shape)
    print(get_luminance(array), get_contrast(array))
    red = get_chanel(array, 0)
    croped = crop(red, 200,300,400,500)
    lum20 = lum(array, 1.2)
    reduce2 = reduce(array,2)
    auto = auto_normalize(array)
    print(get_luminance(auto), get_contrast(auto))
    save(auto, "data/out.jpg")
    array = load("data/rond_blanc.jpg")
    prof = profil(red, 0)
    plt.subplot(211)
    plt.imshow(red, cmap="Reds")
    plt.subplot(212)
    plt.plot(prof)
    plt.show()
