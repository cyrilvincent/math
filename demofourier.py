import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0,1,0,0,0,0,0,0,0,0])
plt.subplot(311)
plt.plot(signal)

tableau_imaginaire = np.fft.fft(signal)
print(tableau_imaginaire)
plt.subplot(312)
plt.plot(np.real(tableau_imaginaire))
plt.subplot(313)
plt.plot(np.imag(tableau_imaginaire))

plt.show()