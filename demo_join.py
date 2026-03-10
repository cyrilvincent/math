import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df = pd.read_csv("data/mesures/mesures.csv")
v_df = df[["T", "VM", "VT"]]
a_df = df[["T", "AM", "AT"]]
join_df = v_df.join(a_df, on="T", rsuffix='_right')
print(join_df)
join_df = pd.merge(v_df, a_df)
print(join_df)