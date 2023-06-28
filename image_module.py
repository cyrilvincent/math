from typing import Tuple

from PIL import Image
import numpy as np
from numpy.typing import NDArray

class ImageLibrary:

    def load(self, path:str) -> np.array :
        im = Image.open(path)
        array = np.asarray(im).astype(float)
        return array

    def save(self, array: NDArray, path: str):
        dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
        dest.save(path)

    def show(self, array: NDArray):
        dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
        dest.show()

    def crop(self, array: NDArray, nb:int) -> np.array:
        if nb < array.shape[0] / 2 and nb < array.shape[1] / 2:
            return array[nb:-nb, nb:-nb]
        else:
            raise ValueError("Nb to large")

    def get_chanel(self, array: NDArray, num: int):
        if 0 <= num < 3:
            return array[:,:,num]
        else:
            raise ValueError("Bad num")

    def add(self, array1: NDArray, array2: NDArray):
        if array1.shape[0] > array2.shape[0]:
            array1 = array1[:array2.shape[0]]
        else:
            array2 = array2[:array1.shape[0]]
        if array1.shape[1] > array2.shape[1]:
            array1 = array1[:, :array2.shape[1]]
        else:
            array2 = array2[:, :array1.shape[1]]
        res = (array1 + array2) / 2
        return res

    # Luminance : mean
    # Facultatif Luminance_by_chanel : mean, mean, mean
    # Contrast : std
    # N&B : mean de la 3d
    # Dynamic : max - min
    # Auto-adjust :
    #   Normalise l'image => (pixel - mean) / std
    #   Appliquer les valeurs idéales => pixel_norm * 63.75 + 127.5
    #   Borner à 0,255 avec np.clip(x,min,max)

    def luminance(self, array: NDArray) -> float:
        return np.mean(array)

    def luminance_3d(self, array: NDArray) -> Tuple:
        return np.mean(array[:,:,0]), np.mean(array[:,:,1]), np.mean(array[:,:,2])

    def contrast(self, array: NDArray) -> float:
        return np.std(array)

    def dynamic(self, array: NDArray) -> float:
        return np.max(array) - np.min(array)

    def black_and_white(self, array: NDArray) -> NDArray:
        return np.mean(array, axis=2)

    def auto_adjust(self, array: NDArray) -> NDArray:
        return np.clip(((array - np.mean(array)) / np.std(array)) * 63.75 + 127.5, 0, 255)


if __name__ == '__main__':
    il = ImageLibrary()
    array = il.load("data/foret.jpg")
    array = il.crop(array, 300)
    # il.show(array)
    array1 = il.load("data/ski.jpg")
    array2 = il.load("data/ski2.jpg")
    res = il.add(array1, array2)
    # il.show(res)
    print(il.luminance(array1))
    print(il.luminance_3d(array))
    print(il.contrast(array1))
    print(il.dynamic(array1))
    il.show(il.black_and_white(array1))
    il.show(il.auto_adjust(array1))
