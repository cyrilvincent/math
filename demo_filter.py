import numpy as np

a = np.random.rand(100000000)
a_filtered = a[a > 0.5]
print(len(a_filtered))

