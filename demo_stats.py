import numpy as np

rnd = np.random.rand(10000000)
print(rnd)
print(np.mean(rnd), np.std(rnd), np.median(rnd), np.quantile(rnd, [0.01,0.1,0.25,0.75,0.99]))

mat22 = np.array([[1,2],[3,4]])
print(np.mean(mat22, axis=0))

# cube (768,1024,3)
# luminance = mean
# contraste = std
# n&b mean axis=2