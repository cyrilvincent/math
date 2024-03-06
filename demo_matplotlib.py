import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
x = range(1000)
y = range(1000)
y2 = np.sin(np.arange(1000) / 100)

plt.subplot(211)
plt.scatter(x, y)
plt.subplot(212)
plt.plot(x, y2, color='green')
plt.show()
#plt.savefig("demo.png")
