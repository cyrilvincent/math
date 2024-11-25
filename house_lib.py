import numpy as np

def load(path):
    data = np.load(path)
    surfaces = data["np_surfaces"]
    loyers = data["np_loyers"]
    return surfaces, loyers

def filter(surface_max, surfaces, loyers):
    predicat = surfaces < surface_max
    return surfaces[predicat], loyers[predicat]