import csv
import numpy as np

with open("data/heartdisease/data_cleaned_up.csv") as f:
    reader = list(csv.DictReader(f))
ages0 = np.array([float(x["age"]) for x in reader if x["num"]=="0"])
sexs0 = np.array([float(x["sex"]) for x in reader if x["num"]=="0"])
trestbps0 = np.array([float(x["trestbps"]) for x in reader if x["num"]=="0"])
chol0 = np.array([float(x["chol"]) for x in reader if x["num"]=="0"])
ages1 = np.array([float(x["age"]) for x in reader if x["num"]=="1"])
sexs1 = np.array([float(x["sex"]) for x in reader if x["num"]=="1"])
trestbps1 = np.array([float(x["trestbps"]) for x in reader if x["num"]=="1"])
chol1 = np.array([float(x["chol"]) for x in reader if x["num"]=="1"])

print(np.mean(ages0), np.mean(ages1))
print(np.mean(sexs0), np.mean(sexs1))
print(np.mean(trestbps0), np.mean(trestbps1))
print(np.min(chol0),np.max(chol1),np.mean(chol0),np.std(chol0), np.mean(chol1),np.std(chol1))