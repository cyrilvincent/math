import pandas as pd
import matplotlib.pyplot as plt
# pip install openpyxl

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
df = pd.read_csv("data/house/house.csv")
print(df)
jena_df = pd.read_csv("data/jena/jena_filtered.csv")
print(jena_df)

df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
df.to_html("data/house/house.html", index=False)
df.to_excel("data/house/house.xlsx", index=False)