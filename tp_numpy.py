# Créer un tableau numpy de -2pi à +2pi avec pas de 0.01
# Appliquer un sin et sauvegarder dans une variable
# idem avec tanh
# Faire sin - tanh

import numpy as np

a = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
sina = np.sin(a)
tanha = np.tanh(a)
diff = sina - tanha
print(diff)
print(np.max(diff))
print(diff[diff > 0])

print(diff.ndim, diff.shape, diff.size, diff.dtype)

for index, value in enumerate(diff):
    print(index, value)
    print(diff[index])

var = 10
print(diff[::10])

# Afficher le sin, la tanh et diff
# Dans le même graphique
# Dans 3 subplots

import matplotlib.pyplot as plt

plt.subplot(311)
plt.plot(a, sina, color="red")
plt.title("Sin")
plt.subplot(312)
plt.plot(a, tanha)
plt.title("Tanh")
plt.subplot(313)
plt.plot(a, diff, color="green")
plt.show()