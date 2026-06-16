import numpy as np
import matplotlib.pyplot as plt

data = np.load("data/jena/jena.npz")
print(data)
preasures = data["p"]
temps = data["t"]
x = np.arange(len(data))

# Afficher les temps el preasures dans un subplot
# Afficher une seul temperature par jour : donc prendre une temperature sur 24

plt.subplot(2,1,1)
plt.title("Temp")
plt.plot(temps[11::24], color="red")
plt.subplot(2,1,2)
plt.title("Preasure")
plt.plot(preasures[11::24])
plt.show()


