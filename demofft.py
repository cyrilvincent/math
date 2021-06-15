import numpy as np
import matplotlib.pyplot as plt

nb = 1j ** 2
print(nb)
nb2 = -5j + 2
print(nb + nb2)
x = 3
j = x*1j

signal = np.array([0.,1,0,0,0,0,0,0,0,0])
transform = np.fft.fft(signal)
print(transform)

plt.subplot(211)
plt.plot(signal)
plt.subplot(212)
plt.plot(np.real(transform))
plt.show()







