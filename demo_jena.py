import numpy as np
import matplotlib.pyplot as plt

dict = np.load("data/jena/jena.npz")
print(list(dict.keys()))
p = dict["p"]
t = dict["t"]
print(p.shape)
x = np.arange(70075)

print(f"Température min: {np.min(t)}, max: {np.max(t)}")

plt.subplot(211)
plt.plot(x, t)
plt.subplot(212)
plt.plot(x, p)
plt.show()

plt.subplot(211)
plt.plot(x[11:365*24:24], t[11:365*24:24])
plt.subplot(212)
plt.plot(x[11:365*24:24], p[11:365*24:24])
plt.show()

x1 = x[11:365*24:24]
t1 = t[11:365*24:24]
p1 = p[11:365*24:24]
x2 = x[365*24+11:2*365*24:24]
t2 = t[365*24+11:2*365*24:24]
p2 = p[365*24+11:2*365*24:24]
t3 = t[2*365*24+11:3*365*24:24]
p3 = p[2*365*24+11:3*365*24:24]
# nb_year = 3
# xtab = np.arange(nb_year, 70075)
# xtab[nb_year - 1] = x[(nb_year - 1)*365*24+11:nb_year*365*24:24]
# t[nb_year - 1] = t[(nb_year - 1)*365*24+11:nb_year*365*24:24]
# p[nb_year - 1] = p[(nb_year - 1)*365*24+11:nb_year*365*24:24]

print(f"Température année 1 min: {np.min(t1)}, max: {np.max(t1)}")
print(f"Température année 2 min: {np.min(t2)}, max: {np.max(t2)}")
print(f"Température année 3 min: {np.min(t3)}, max: {np.max(t3)}")

tp = t/p
print(tp)

# TP
# Afficher dans 2 diagrammes les temperatures et pressions
# Calculer la temperature min, max
# Afficher les temperatures par jour (prendre une temperature sur 24)
# Idem, mais commencer par la temperature de midi
# Afficher les temperatures de la 1ère année uniquement
# Calculer le min et max de temperature de l'année 1, 2 et 3
# Créer le vecteur tp qui est t/p

