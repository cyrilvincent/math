import numpy as np
import matplotlib.pyplot as plt

signal = np.array([0,1,0,0,0,0,0,0,0,0,0])
result = np.fft.irfft(signal)

plt.plot(np.real(result))
plt.show()