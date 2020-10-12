import csv

with open("data/covid/covid-france.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row["NbCas"]) != 0:
            print(float(row["DC"]) / float(row["NbCas"]))