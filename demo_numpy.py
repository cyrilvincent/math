import numpy as np

a1 = np.array([1,2,3,4], dtype=np.float64)
print(a1)

# for i in np.arange(-2*np.pi, 2*np.pi, 0.1):
#     print(np.sin(i))

rnd = np.random.rand(10)
print(rnd * 10)
print(np.random.randint(0,100,10))

a2 = np.arange(4)
a3 = a1 * a2
print(np.sin(a3))
np.round(a1,2)

abytes = np.array([1,2,3,4,255], dtype=np.uint8)
print(abytes + 1)

print(rnd)
for value in rnd:
    print(value)
for i in range(len(rnd)):
    print(rnd[i])

print(np.sum(a1))
print(a1.sum())

print(a1.dtype, a1.ndim, a1.size, a1.shape)

a100 = np.arange(100)
print(a100[89:3:-2])

rnd10 = np.random.rand(10)
a10 = np.arange(10)
filter = rnd10>0.5
print(filter)
print(a10[filter])

