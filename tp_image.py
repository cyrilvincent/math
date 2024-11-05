# Charger une image avec Pillow et la convertir en numpy
# Obtenir et afficher le canal vert
# Croper l'image : enlever 10 pixels au nord, sud, est ouest
# Diviser la taille de l'image par 4 : prendre 1 ligne sur 2 et 1 colonne sur 2
# Transpose
# Bonus : tout mettre dans des fonctions get_chanel(0 ou 1 ou 2), crop(10,10,10,10)
import numpy as np
from PIL import Image

def load(path: str) -> np.ndarray:
    im = Image.open(path)
    array = np.asarray(im).astype(np.float64)
    return array

def save(array: np.ndarray, path: str):
    dest = Image.fromarray(array.astype(np.uint8)).convert("RGB")
    dest.save(path)

def get_chanel(array: np.ndarray, num: int) -> np.ndarray:
    return array[:,:,num]

def crop(array, north: int, south: int, east: int, west: int) -> np.ndarray:
    return array[north:-south, east:-west]

def divide(array, factor: int):
    step = int(np.sqrt(factor))
    return array[::step, ::step]

def transpose(array):
    return array.T

def luminance(array) -> float:
    pass # mean de l'array

def contrast(array) -> float:
    pass # std

def auto_lum(array) -> np.ndarray:
    # Ramène la luminnce à 127.5
    np.clip(array, 0, 255)

# Bonus
def auto_lum_contrast(array) -> np.ndarray:
    # Lum parfaite = 127.5, contraste parfait = 63.75

if __name__ == '__main__':
    array = load("data/ski.jpg")
    print(array.shape)
    array_nb = get_chanel(array, 1)
    array_crop = crop(array_nb, 50, 100, 150, 200)
    array_divide = divide(array_nb, 4)
    array_transpose = transpose(array_divide)
    save(array_transpose, "data/out.jpg")
