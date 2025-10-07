# Charger avec pandas data/heartdisease/data_cleaned_up
# Describe
# Créer le dataframe ok = num=0
# Créer le dataframe ko = num=1
# Refaire les describe
# Correlation, de pearson = dataframe.corr()
# Conclusion
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option("display.expand_frame_repr", False)

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
print(dataframe.describe())

ok = dataframe[dataframe["num"] == 0]
ko = dataframe[dataframe["num"] == 1]

print(ok.describe())
print(ko.describe())

print(dataframe.corr())

