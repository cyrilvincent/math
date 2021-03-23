import numpy as np
import matplotlib.pyplot as plt

i1 = 3+2j
i2 = -4-2.5j
print(i1 + i2)
print(i1 * i2)
print(1j ** 2)

signal = np.array([0,1,0,0,0,0,0,0,0,0,0])
transformee = np.fft.fft(signal)
print(transformee)
plt.subplot(211)
plt.plot(signal)
plt.subplot(212)
plt.plot(np.real(transformee))
plt.show()

f = lambda x : 2* np.cos(2 * np.pi * x / 2)
g = lambda x : np.sin(2 * np.pi * x / 5)
dt = 0.1
x = np.arange(0,10,dt)
y = f(x) + g(x)
plt.subplot(311)
plt.plot(x, f(x))
plt.subplot(312)
plt.plot(x, g(x))
plt.subplot(313)
plt.plot(x, y)
plt.show()

res = np.fft.fft(y)
freq = np.fft.fftfreq(y.size, d=dt)
plt.plot(np.abs(freq), np.abs(res.real), label="real")
plt.plot(np.abs(freq), np.abs(res.imag), label="imag")
plt.show()
