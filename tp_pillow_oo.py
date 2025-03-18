import numpy as np
from PIL import Image # pip install Pillow
import matplotlib.pyplot as plt
import my_library

# création de la classe
# indentation de toutes les fonctions
# ajout de sel comme 1er paramètre
# préfixer les appels de méthode par self.
# Création de la méthode __init__() qui possède l'attribut array
# Virer array des paramètres des méthodes
# Prefixer les appels à array par self.

class ImageService:

    def __init__(self):
        self.array = None

    def open(self, path):
        """
        Open the file
        :param path: the path of the file
        """
        im = Image.open(path)
        self.array = np.asarray(im).astype(np.float64)

    def save(self, path):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.save(path)

    def get_chanel(self, num):
        """
        Return the chanel
        :param num: Must be 0,1 or 2
        :return: numpy matrix
        """
        self.array = self.array[:,:,num]
        return self.array

    def crop(self, top, bottom, left, right):
        self.array = self.array[top:-bottom, left:-right]

    def sub_sampling(self, row, col):
        self.array = self.array[::row, ::col]

    def negative(self):
        self.array = np.abs(self.array - 255)

    def flip(self, horizontal=True):
        if horizontal:
            self.array = self.array[::-1]
        else:
            self.array = self.array[:, ::-1]

    def luminance(self):
        return np.mean(self.array)

    def luminance3(self):
        return np.mean(self.get_chanel(0)), np.mean(self.get_chanel(1)), np.mean(self.get_chanel(2))

    def contrast(self):
        return np.std(self.array)

    def profile(self, horizontal=True):
        if horizontal:
            return np.mean(self.array, axis=0)
        else:
            return np.mean(self.array, axis=1)

    def black_white(self):
        self.array = np.mean(self.array, axis=2)

    def auto_lum_contrast(self, sigmoid=True):
        norm = (self.array - self.luminance()) / self.contrast()
        denorm = norm * 255/4 + 127.5
        if not sigmoid:
            return np.clip(denorm, 0, 255)
        else:
            return my_library.sigmoid(denorm / 255) * 255


# open(path)
# save(array, path)
# get_chanel(array, 0) => red
# crop(array, top, bottom, left, right)
# sub_sampling(array, 2,2) si j'ai 1000x500 => 500x250
# negative(array)
# flip(array, horizontal=True)
# luminance = mean = 127.5
# contraste = std = 255/4
# profil(horizontal=True)
# black_white =
# auto_lum_contrast = ((x - mean) / std) * 255/4 + 127.5 : sans clip, puis avec np.clip puis avec sigmoid
if __name__ == '__main__':
    service = ImageService()
    service.open("data/ski.jpg")
    service.crop(50,100,150,200)
    service.sub_sampling(2,2)
    service.negative()
    service.save("data/out.jpg")
    service.get_chanel()

