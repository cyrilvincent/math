import matplotlib.pyplot as plt

plt.subplot(121)
plt.bar(range(10), range(10))
plt.subplot(122)
plt.scatter(range(10), range(10))
plt.savefig("myfig.png")
plt.show()