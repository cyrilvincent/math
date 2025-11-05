import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# pip install openpyxl

df = pd.read_csv("data/house/house.csv",sep=",")
# df = pd.read_excel("data/house/house.xlsx",sheet_name="Sheet1")
df["loyer_m2"]=df["loyer"]/df["surface"]

