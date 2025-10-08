import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
# pip install scipy

x = np.arange(100)
y = 2. * x + 1
y += (np.random.rand(100) - 0.5) * 20

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
print(slope, intercept, rvalue, pvalue, stderr)
y2 = slope * x + intercept

plt.scatter(x, y)
plt.plot(x, y2, color="red")
plt.show()
