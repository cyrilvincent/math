import numpy as np
from PIL import Image # pip install Pillow

class ImageService:

    def __init__(self, path):
        self.path = path
        im = Image.open(path)
        self.array = np.asarray(im).astype(np.float64)

    def save(self, path):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.save(path)

    def show(self):
        dest = Image.fromarray(self.array.astype(np.uint8)).convert("RGB")
        dest.show()

    def transpose(self):
        self.array = np.swapaxes(self.array, 0,1)

    def get_chanel(self, num):
        self.array = self.array[:,:,num]

    def crop(self, north, south, east, west):
        self.array = self.array[north:-south, west:-east]

    def reduct(self, n:int):
        self.array = self.array[::n,::n]

    def change_lum(self, delta):
        self.array = np.clip(self.array + delta, 0, 255)

    def change_lambda(self, fn):
        self.array = np.clip(fn(self.array), 0, 255)

    def add(self, array2):
        if self.array.shape[0] > array2.shape[0]:
            self.array = self.array[:array2.shape[0]]
        else:
            array2 = array2[:self.array.shape[0]]
        if self.array.shape[1] > array2.shape[1]:
            self.array = self.array[:, :array2.shape[1]]
        else:
            array2 = array2[:, :self.array.shape[1]]
        self.array = (self.array + array2) / 2


if __name__ == '__main__':
    image_service = ImageService("data/ski.jpg")
    image_service.transpose()
    image_service.get_chanel(0)
    image_service.crop(150,150,50,50)
    image_service.reduct(2)
    image_service.change_lum(-50)
    image_service.change_lambda(lambda x: (np.tanh((x - 127.5) / 64) + 1) * 127.5)
    image_service = ImageService("data/ski.jpg")
    image_service2 = ImageService("data/mug.jpg")
    image_service.add(image_service2.array)
    image_service.show()