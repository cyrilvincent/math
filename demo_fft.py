import numpy as np
import matplotlib.pyplot as plt

c = 1 + 2j
c2 = 1 + 1j
imag = 1j
print(imag ** 2)
print(c + c2)

signal = np.zeros(10)
signal[1] = 1

transformed = np.fft.fft(signal)
plt.subplot(211)
plt.plot(signal)
plt.subplot(212)
plt.plot(np.real(transformed), color="red")
plt.show()
