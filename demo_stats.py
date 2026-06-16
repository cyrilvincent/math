import numpy as np

rnd = np.random.rand(10000)
print(rnd.mean(), np.median(rnd), np.quantile(rnd, [0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]))

v = np.array([1,2,3,4,5,np.nan])
print(v)
print(np.mean(v), np.nanmean(v))

print(1j ** 2)

c1 = 2 + 3.5j
c2 = 4.5 - 2j
print(c1 + c2)
