import csv
from typing import Tuple

import numpy as np

def load_house(path: str) -> Tuple:
    """
    Load house
    :param path: the path
    :return: 2 np arrays surfaces, loyers
    """
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        surfaces = []  # np.array([])
        loyers = []
        for row in reader:
            surface = float(row["surface"])
            surfaces.append(surface)
            loyer = float(row["loyer"])
            loyers.append(loyer)
    np_surfaces = np.array(surfaces)
    np_loyers = np.array(loyers)
    return np_surfaces, np_loyers
