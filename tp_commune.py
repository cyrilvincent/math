import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

depts = pd.read_csv("data/communes/dept.csv")  #, index_col="id")
depts["dept_id"] = depts["id"]

communes = pd.read_csv("data/communes/communes.csv", low_memory=False)


df = communes.join(depts, on="dept_id", rsuffix="_right")
df.to_excel("data/communes/out.xlsx")

gre = df[df["id"] == 38185]

print(gre)

# join( on="dept_id")

# Joindre dept + communes
# Filtrer lea commune de Grenoble (38185)
# Bonus : joindre les iris
# Bonus joindre les CP
