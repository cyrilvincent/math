import matplotlib.pyplot as plt
import matplotlib
import math

print(matplotlib.__version__)
xplot = range(1000)
yplot = [math.sin(x / 500) for x in xplot]
yplot2 = [math.cos(x / 1000) for x in xplot]
plt.plot(xplot, yplot)
plt.plot(xplot, yplot2)

plt.show()

