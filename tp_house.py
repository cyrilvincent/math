import numpy as np

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

print(rnd.sort())

# Créer le tableau loyers_sorted
# Prendre les 10 derniers loyers et les afficher
# Afficher les loyers_sorted du 10ème au 30ème avec un pas de 2
# Afficher les loyers d'index impairs
# Afficher les loyers dans l'ordre inverse
# Filtrer les loyers et surfaces > loyer moyen