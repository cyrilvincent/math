import numpy as np

print(np.__version__)

v1 = np.array([1.,2,3,4])
v2 = np.array([5,6,7,8])
v3 = v1 + v2
print(v3)
v4 = v1 * v2
print(v4)
print(v1 ** 2)
print(v1 * 2)
print(v1 % 2 == 0)

# Add
# Function
print(v1 + v2)
# Procedure
print(np.add(v1, v2))
# OO
print(v1.__add__(v2))

print(np.sin(v1))

# dot
# Produit scalaire
print(np.dot(v1, v2))
print(v1.dot(v2))



