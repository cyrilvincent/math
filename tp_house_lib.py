import numpy as np

def load(path: str) -> tuple:
    data = np.load(path)
    surfaces = data["np_surfaces"]
    loyers = data["np_loyers"]
    return surfaces, loyers

def stats(array) -> tuple:
    min = np.min(array)
    max = np.max(array)
    return min, max

def compute_loyers_m2(loyers, surfaces):
    return loyers / surfaces

def filter_by_surface(loyers, surfaces, surface_thresold) -> tuple[np.ndarray, np.ndarray]:
    return surfaces[surfaces < surface_thresold], loyers[surfaces < surface_thresold]