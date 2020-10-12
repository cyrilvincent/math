import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
x = [0,1,2,3,4]
y = [2.0,5.1,6.66,-2,12]
plt.subplot(221)
plt.scatter(x, y)
plt.subplot(222)
plt.plot(x, y)
plt.subplot(223)
plt.bar(x, y)
plt.show()