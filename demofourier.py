i = 1j ** 2
print(i)
x = 3+2j
import numpy as np
import matplotlib.pyplot as plt
print(x, np.real(x), np.imag(x))

v1 = np.array([0,1.,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
plt.subplot(211)
plt.plot(v1)

res1 = np.fft.fft(v1)
print(res1)
plt.subplot(212)
plt.plot(np.real(res1))

plt.show()

