from scipy.io import wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

rate, data = wav.read('data/wav/7-bells.wav')
print(rate, data.shape)
if len(data.shape) == 2 and data.shape[1] == 2: #Because stereo
    data = data[:, 0]
fft_out = np.fft.fft(data)
print(fft_out.shape)
plt.plot(np.abs(np.fft.fftfreq(data.size, 1 / 44100)), np.abs(np.real(fft_out)))
plt.xscale("log")
plt.show()