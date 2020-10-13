import numpy as np
v1 = np.random.rand(10000)
print(np.mean(v1))
print(np.std(v1))
print(np.var(v1))
print(np.median(v1))
print(np.quantile(v1, [0.25]))