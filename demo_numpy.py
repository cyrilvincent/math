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

print(np.max(v1))

vrandom = np.random.randint(10, size=6)
print(vrandom)
print(vrandom.size, vrandom.ndim, vrandom.shape, vrandom.dtype)
# verror = np.array([0, 1])
# print(vrandom + verror)

v1 = np.array([1.,2,3,4])
print(v1[1], v1[-1], v1[1:3], v1[1:-1], v1[1:], v1[:3], v1[:])
# step
print(v1[1:4:2], v1[:-1:2], v1[1::2], v1[::2])

# TP
# Créer un vecteur aléatoire de 10 floats compris entre 0 et 400
# Afficher le nuage de point (scatter) dans matplotlib
# Afficher le min et le max
# A l'aide du tp house.csv créer l'array surfaces et loyers
# Afficher le shape des vecteurs
# Créer facilement l'array loyer_m2
# Afficher le loyer_m2 min et max
# Afficher 1 loyer sur 3 sauf les 2 premiers et les 2 derniers






