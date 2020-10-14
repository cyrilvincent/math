import pandas

#dataframe = pandas.read_csv("data/mesures/mesures.csv")
dataframe = pandas.read_excel("data/mesures/mesures.xlsx", sheet_name="CSV")
serie = dataframe.VM
# serie = dataframe["VM"]
# serie = dataframe[4]
# serie = serie[serie > 0]
# print(serie)
print(dataframe)

