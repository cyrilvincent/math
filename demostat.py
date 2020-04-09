import numpy as np
v1 = np.random.rand(10000)
print(np.mean(v1))
print(np.std(v1))
print(np.var(v1))

mat1 = np.random.rand(100,100000)
sommes = np.sum(mat1, 0)
print(sommes)

# import matplotlib.pyplot as plt
# plt.subplot(211)
# plt.scatter(range(100000), sommes)
# plt.subplot(212)
# plt.hist(sommes, bins=100)
# plt.show()
print(np.mean(sommes))
print(np.std(sommes))
print(np.median(sommes))
print(np.quantile(sommes,[0.25,0.5,0.75,1]))