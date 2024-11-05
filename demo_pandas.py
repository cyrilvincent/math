import pandas as pd

df = pd.read_csv("data/house/house.csv")
pd.read_csv()
df["loyer_m2"] = df.loyer / df["surface"]
df = df[df.surface < 200]
print(df)
df.to_html("data/house/house.html")
df.to_excel("data/house/house.xlsx")
print(df.describe())