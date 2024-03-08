import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np

y = np.array([0,1,0,0,0,0,0,0,0,0])
x = np.arange(10)
y2 = np.array(fft.fft(y))
print(y2)
print(1j**2)

complex = 3+2j
print(complex)
print(np.real(complex), np.imag(complex))

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
