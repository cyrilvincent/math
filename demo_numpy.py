import numpy as np

print(np.__version__)

a1 = np.arange(0.1, 10.2, 0.1)
print(a1)
a2 = np.round(np.linspace(0, 10, 10), 2)
print(a2)

np.random.seed(42)
rnd1 = np.random.rand(10)
print(rnd1)
rnd2 = np.random.randint(0, 100, 10)
print(rnd2)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a*b)
print(np.cos(b))
print(np.sum(a), a.sum())

print(a.ndim, a.size, a.shape, a.dtype)

v100 = np.arange(100, 200)
for value in v100:
    print(value)
for i in range(len(v100)):
    print(v100[i])

print(v100[50:])
v100[0]=999
print(v100)

v101 = np.append(v100, -1)
print(v101)
print(np.insert(v100, 5, -99))

print(v100[(np.cos(v100) > 0) | (v100 % 3 == 0)])

filter = v100 % 2 == 0
print(filter)
print(v100[filter])

result = v100 * 10 + 2



