import numpy as np
import matplotlib.pyplot as plt

class Mesure:

    def __init__(self, path) -> None:
        """
        Blah blah
        """
        self.path = path # Attribute
        self.vm = None
        self.vt = None
        self.t = None

    def load(self):
        """
        Load the NPZ
        """
        dict = np.load(self.path)
        self.vm = dict["vm"]
        self.vt = dict["vt"]
        self.t = dict["t"]

    def min(self, name: str):
        if name == "vm":
            return np.min(self.vm)
        elif name == "vt":
            return np.min(self.vt)
        else:
            return "Error"
        
    def save(self, path:str):
        np.savez(path, vm=self.vm, vt=self.vt)

    def diff(self):
        return self.t[np.abs(self.vm - self.vt) > 0], self.vm[np.abs(self.vm - self.vt) > 0]



if __name__=='__main__':
    mesure1 = Mesure("data/mesures/mesures.npz")
    mesure1.load()
    print(mesure1.vm)
    print(mesure1.vt)
    print(mesure1.min("vm"))
    mesure1.save("data/mesures/mesures2.npz")
    res = mesure1.diff()
    print(res)