import numpy as np
import matplotlib.pyplot as plt
print(1j ** 2)
c1 = 2 + 3j
c2 = 1.4 + 2.5j
print(c1 + c2)
print(c1 * c2)
print(c1 + np.inf)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0])
plt.subplot(211)
plt.plot(signal)
result = np.fft.fft(signal)
print(result)
plt.subplot(212)
plt.plot(np.real(result))
plt.show()

