import pandas as pd

depts = pd.read_csv("data/communes/dept.csv")  #, index_col="id")
depts["dep_id"] = depts["id"]
print(depts)

# join( on="dept_id")

# Joindre dept + communes
# Filtrer lea commune de Grenoble (38185)
# Bonus : joindre les iris
# Bonus joindre les CP
