import numpy as np
import matplotlib.pyplot as plt

x = np.inf

print(2 * x)
print(2 / x)

v1 = np.array([1,2,3,np.nan,5])
print(v1)
print(np.sum(v1))
print(np.nansum(v1))

print(1j ** 2)
c1 = 3 + 2j
c2 = -5 + 4j
print(c1 + c2)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0])
result = np.fft.fft(signal)
print(result)
plt.subplot(211)
plt.plot(signal)
plt.subplot(212)
plt.plot(np.real(result))
plt.show()