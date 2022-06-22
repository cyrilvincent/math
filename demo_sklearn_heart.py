import sklearn
import sklearn.linear_model as lm
import sklearn.neighbors as nn
import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", axis=1)

# model = lm.LinearRegression()
for k in range(1,12):
    model = nn.KNeighborsClassifier(n_neighbors=k)
    model.fit(x, y)
    predicted = model.predict(x)
# print(model.coef_, model.intercept_)

    score = model.score(x, y)
    print(f"Score: {score}")
