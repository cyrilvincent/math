import numpy as np

rnd = np.random.rand(1000)
print(np.mean(rnd), np.std(rnd), np.median(rnd), np.quantile(rnd, [0.1, 0.25, 0.5, 0.75]))