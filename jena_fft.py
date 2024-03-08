import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class JenaFFT:

    def __init__(self) -> None:
        self.t = []
        self.nb_t = 0
        self.dataframe = pd.DataFrame()

    def load(self, path: str):
        self.dataframe = pd.read_csv(path)
        self.t = self.dataframe["T (degC)"]
        self.nb_t = len(self.t)
        self.x = np.arange(self.nb_t)
        self.nb_years = self.nb_t / (24*365)
        self.nb_per_year = self.x / self.nb_years

    def fft(self):
        fft = np.fft.fft(self.t)
        return np.abs(fft)
    
    def show(self, fft):
        plt.subplot(211)
        plt.plot(self.x, self.t)
        plt.subplot(212)
        plt.step(self.nb_per_year, fft)
        plt.xscale('log')
        plt.xticks([1, 365], labels=['1/Year', '1/day'])
        plt.xlabel('Frequency (log scale)')
        plt.show()

if __name__=='__main__':
    jena = JenaFFT()
    jena.load("data/jena/jena_filtered.csv")
    fft = jena.fft()
    jena.show(fft)