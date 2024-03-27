import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

dataframe = pd.read_csv("data/jena/jena_filtered.csv")
t = dataframe["T (degC)"]
print(t.describe())

# Prendre un t toutes les 24h, à midi
# Afficher le plot
# Appliquer une fft et afficher la partie réelle
# Refaire sans le filtre de 24h


