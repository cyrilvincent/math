from PIL import Image
import numpy as np
from numpy.typing import NDArray

class ImageTreatment:

    def __init__(self, path:str) -> None:
        self.path = path
        self.array = np.array([])

    def load(self):
        im = Image.open(self.path)
        self.array = np.asarray(im).astype(np.float64)

    def save(self, new_path:str, array: NDArray[np.float64], mode:str="RGB"):
        dest = Image.fromarray(array.astype(np.uint8)).convert(mode)
        dest.save(new_path)

    def show(self, array: NDArray[np.float64]):
        dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
        dest.show()

    def crop(self, north: int, south: int, east: int, west:int) -> NDArray[np.float64]:
        array = self.array[north:-south,west:-east]
        return array
    
    def transpose(self) -> NDArray[np.float64]:
        return np.moveaxis(self.array, 0,1)
    
    def get_chanel(self, num: int) -> NDArray[np.float64]:
        return self.array[:,:,num]
    
    def dynamic(self, num_chanel) -> np.float64:
        return np.max(self.array[:,:,num_chanel]) - np.min(self.array[:,:,num_chanel])
    
    def reduct(self, n:int) -> NDArray[np.float64]:
        return self.array[::n,::n,:]
    
    def change_lum(self, delta_lum: np.float64) -> NDArray[np.float64]:
        return np.clip(self.array + delta_lum, 0, 255)
    
    def add(self, array):
        if array.shape[0] > self.array.shape[0]:
            array = array[:self.array.shape[0], :self.array.shape[1], :]
            return (array + self.array) / 2
        else:
            temp = self.array[:array.shape[0], :array.shape[1], :]
            return (array + temp) / 2
        
    def luminance_contrast(self):
        return np.mean(self.array), np.std(self.array)
    
    def median_quartiles(self):
        return np.median(self.array), np.quantile(self.array, [0.25,0.75])
    
    def autolum(self):
        lum = np.mean(self.array)
        return self.change_lum(127.5 - lum)
    
    def auto_lum_contrast(self):
        lum = np.mean(self.array)
        contrast = np.std(self.array)
        return np.clip(((self.array - lum) / contrast) * 63.75 + 127.5,0,255)
    
    def black_white(self):
        return np.mean(self.array, axis=2)
    
    def horizontal_profile(self):
        return np.mean(self.array, axis=0)

        
    def __del__(self):
        pass
        
           
    

if __name__=='__main__':
    obj = ImageTreatment("data/ski.jpg")
    obj.load()
    array = obj.crop(10,20,40,80)
    #obj.show(array)
    array = obj.transpose()
    #obj.show(array)
    array = obj.get_chanel(0)
    #obj.show(array)
    print(obj.dynamic(0))
    array = obj.reduct(2)
    # obj.show(array)
    # array = obj.change_lum(-100)
    #obj.show(array)
    obj2 = ImageTreatment("data/mug.jpg")
    obj2.load()
    array = obj.add(obj2.array)
    # obj.show(array)
    print(obj.luminance_contrast())
    print(obj.median_quartiles())
    array = obj.auto_lum_contrast()
    obj.show(array)
    print(obj.array.shape)
    array = obj.black_white()
    print(array.shape)
    obj.show(array)



        

    

    

