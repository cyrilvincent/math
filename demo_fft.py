import numpy as np
import matplotlib.pyplot as plt

i1 = 3+2j
print(i1)
i2 = 1j
print(i2**2)
print(i1 + i2)
print(i1 * i2)

signal = [0,1.0,0,0,0,0,0,0,0]
plt.subplot(311)
plt.plot(signal)


fourier = np.fft.fft(signal)
print(fourier)
print(fourier.shape)
plt.subplot(312)
plt.plot(np.real(fourier))
plt.subplot(313)
plt.plot(np.imag(fourier))

plt.show()


