import numpy as np
import matplotlib.pyplot as plt

a = 1j
print(a ** 2)
b = 3 + 2j
print(b)
c = 2 - 0.5j
print(b+c)

v1 = np.array([0.,1,0,0,0,0,0,0,0,0,0])
plt.subplot(311)
plt.plot(v1)
res = np.fft.fft(v1)
print(res.shape)
print(res)
plt.subplot(312)
plt.plot(np.real(res))
plt.subplot(313)
plt.plot(np.imag(res))
plt.show()
