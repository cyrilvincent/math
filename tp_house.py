import numpy as np
import matplotlib.pyplot as plt

dico = np.load("data/house/house.npz")
print(dico)
loyers = dico["np_loyers"]
surfaces = dico["np_surfaces"]
print(loyers.size)

loyers_m2 = loyers / surfaces
print(loyers_m2)

print(np.mean(loyers), np.mean(surfaces), np.mean(loyers_m2))

print(loyers.ndim, loyers.shape)

print(loyers[1], loyers[loyers.size - 1])
# <=>
print(loyers[1], loyers[-1])
for loyer in loyers[::-2]:
    print(loyer)
# i=0
# while i < loyers.size:
#     print(loyers[i])
#     i+=1

a = np.arange(5)
print(a[2:5])

rnd = np.random.rand(10)
x = np.arange(10)
print(x, rnd)

predicate = rnd > 0.5
print(predicate)
print(x[predicate], rnd[predicate])
print(x[rnd>0.5], rnd[rnd>0.5])

def f(x):
    return 2 * x + 1

print(f(rnd[rnd>0.5]))
rnd.sort()
print(rnd)

plt.scatter(surfaces, loyers)
plt.show()

# Créer le tableau loyers_sorted
# Prendre les 10 derniers loyers et les afficher
# Afficher les loyers_sorted du 10ème au 30ème avec un pas de 2
# Afficher les loyers d'index impairs
# Afficher les loyers dans l'ordre inverse
# Filtrer les loyers et surfaces > loyer moyen
# Créer la fonction f(x) = x ** 2 - 2 + x + 1 et appliquer cette fonction aux loyers
# Créer la fonction g(x) = moyenne_tarif_m2 * x et appliquer cette fonction aux surfaces

loyers_sorted = loyers.copy()
loyers_sorted.sort()
print(loyers_sorted[-10:])
print(loyers_sorted[10:31:2])
print(loyers[1::2])
print(loyers_sorted[::-1])
average = np.mean(loyers)
average_m2 = np.mean(loyers_m2)
loyers_filtered = loyers[loyers > average]
surfaces_filtered = surfaces[loyers > average]
print(loyers_filtered, surfaces_filtered)

def f(x):
    return x ** 2 + x + 1

def g(x):
    return x * average_m2

print(f(loyers))

print(loyers / g(surfaces))

# Afficher g(surfaces) en vert
