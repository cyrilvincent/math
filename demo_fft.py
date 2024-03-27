import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np

imag1 = 3+2j
imag2 = 1j
print(imag2 ** 2)
print(imag1 + imag2)

serie = np.array([0,1,0,0,0,0,0,0,0,0])
res = fft.fft(serie)
print(res)

plt.subplot(311)
plt.plot(np.arange(10), serie)
plt.subplot(312)
plt.plot(np.arange(10), np.real(res))
plt.subplot(313)
plt.plot(np.real(res), np.imag(res))
plt.show()