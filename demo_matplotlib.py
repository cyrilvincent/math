import matplotlib.pyplot as plt
import math

fn = lambda x: math.sin(x / 100)
fn2 = lambda x: math.cos(x / 100)
x = range(100)
y = [fn(value) for value in x]
y2 = [fn2(value) for value in x]
plt.subplot(121)
plt.scatter(x, y, color="red")
plt.subplot(122)
plt.bar(x, y2, color="green")
plt.show()