import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pip install openpyxl

df = pd.read_excel("data/mesures/mesures.xlsx", index_col="T")
print(df)

# Afficher VT et VM
# diff = |VT - VM|
# Afficher diff

