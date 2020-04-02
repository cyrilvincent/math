import matplotlib.pyplot as plt

y = range(100,200,2)
x = range(50)

plt.subplot(221)
plt.scatter(x,y)

l = [2.0,5.0,6.66,25,-12]
x = [1,2,3,4,5]
plt.subplot(222)
plt.bar(x,l)

l = [2.0,5.0,6.66,25,-12]
x = [1,2,3,4,5]
plt.subplot(223)
plt.bar(x,l)

l = [2.0,5.0,6.66,25,-12]
x = [1,2,3,4,5]
plt.subplot(224)
plt.bar(x,l)

plt.show()