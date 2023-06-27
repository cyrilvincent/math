import csv
import numpy as np

class HouseService:

    def load_house(self, path):
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