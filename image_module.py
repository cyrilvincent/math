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

if __name__ == '__main__':
    il = ImageLibrary()
    array = il.load("data/foret.jpg")
    array = il.crop(array, 300)
    il.show(array)
    array1 = il.load("data/ski.jpg")
    array2 = il.load("data/ski2.jpg")
    res = il.add(array1, array2)
    il.show(res)
