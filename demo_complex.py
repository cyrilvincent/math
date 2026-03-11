i = 1j
print(i ** 2)

c1 = 3 - 2j
print(c1 + i)

import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0])
result = np.fft.fft(signal)
plt.subplot(2,1,1)
plt.plot(signal)
plt.subplot(2,1,2)
plt.plot(np.real(result))
plt.show()
