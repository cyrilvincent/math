import pandas as pd

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
print(dataframe.describe())
print(dataframe.loyer)
dataframe["loyer_par_m2"] = dataframe.loyer / dataframe.surface
print(dataframe)
dataframe.to_html("data/house/house.html")
with pd.ExcelWriter("data/house/house.xlsx",
                    mode='a', if_sheet_exists='overlay') as writer:
    dataframe.to_excel(writer, startcol=2, startrow=2, sheet_name="Toto" , index=False) # pip install openpyxl