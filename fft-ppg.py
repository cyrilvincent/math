import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data/heartdisease/ppg.csv") as f:
    reader = list(csv.DictReader(f))
    ppg1 = [float(row["PPG"])
             for row in reader
             if row["PPG"] != None and row["PPG"] != "nan"]
    windowSize = 2048
    for i in range(0,len(ppg1),int(windowSize / 2)):
        window = np.array(ppg1[i:i+windowSize])
        plt.subplot(211)
        plt.plot(window)
        res = np.fft.fft(window)
        plt.subplot(212)
        plt.axis([0,10,0,1e6])
        plt.plot(np.abs(res))
        plt.show()