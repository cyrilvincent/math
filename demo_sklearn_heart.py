import sklearn
import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataframe.num
x = dataframe.drop("num", axis=1)

print(sklearn.__version__)
model = lm.LinearRegression()
model.fit(x, y)
predicted = model.predict(x)
print(model.coef_, model.intercept_)

score = model.score(x, y)
print(f"Score: {score}")


# plt.scatter(dataframe.surface, dataframe.loyer)
# plt.plot(np.arange(400), predicted)
# plt.show()


