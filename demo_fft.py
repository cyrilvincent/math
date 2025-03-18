import numpy as np
import matplotlib.pyplot as plt

c1 = 1j ** 2
print(c1)
c2 = 2 - 3j
print(c1 + c2)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0])
res = np.fft.fft(signal)
print(res)
plt.plot(np.real(res))
plt.show()