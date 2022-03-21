import numpy as np

a1 = np.arange(10)
print(list(filter(lambda x: x % 2 == 0, a1)))
print([x for x in a1 if x % 2 == 0])

b1 = [True, False, True, False, True, True, False, True, False, True]
print(b1)
print(a1[b1])
print(a1 < 5)
print(a1[a1 % 2 == 0])


