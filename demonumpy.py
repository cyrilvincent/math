import numpy as np
print(np.__version__)

v1 = np.array([1,2,3,4])
v2 = np.arange(5,9)
print(v1, v2, v1 * v2)
print(np.sin(v1))

print(v1.sum())
print(np.sum(v1))
# Repren,dre le tp précédent
np.random.seed(0)
x1 = np.random.rand(5) * 10
print(x1)
print("nombre de dimensions de x1: ", x1.ndim)
print("forme de x1: ", x1.shape)
print("taille de x1: ", x1.size)
print("type de x1: ", x1.dtype)
#print(np.random.shuffle(x1)[:10])
sup5_filter = x1 > 5 and x1 < 8
sup5 = x1[sup5_filter]
#res = x1[[True, False,False,False,True]]
print(sup5)


