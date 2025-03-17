import numpy as np
import my_library as lib

print(np.__version__)

a1 = np.array([1, 2, 3, 4])
a1 = a1.astype(np.uint8)
print(a1 + 253)


a2 = np.arange(1, 10, 2)
print(a2)

a3 = np.linspace(0, 9.9, 10)
print(a3)

rnd = np.random.rand(10)
print((rnd * 10).astype(np.int16))
rnd2 = np.random.randint(0, 10, 20)
print(rnd2)

np.random.seed(42)
rnd3 = np.abs(np.random.randint(0,256,10)).astype(np.uint8)
print(rnd3)

a1 = np.array([1,2,3,4])
a2 = np.arange(4)
print(a1, a2, a1 + a2)
a3 = np.arange(10)
# print(a1+a3)
print(np.sin(a1) * 2)

print(lib.sigmoid(a1))
print(np.sum(a1))

print(a1.dtype, a1.ndim, a1.size, a1.shape)

rnd = np.random.rand(10)
print(rnd)
print(rnd[-1])
for i in range(rnd.size):  # For par indexation à éviter
    print(rnd[i])

for v in rnd:  # For par valeur, à utiliser
    print(v)

# Slice = subset
for i in range(2, 8): # Mauvais
    print(rnd[i])

print(rnd[2:8:2])
print(rnd[1:-1:3])
print(rnd[::-1])


print(rnd[rnd > 0.5])
predicate = rnd > 0.5
print(predicate)
print(rnd[predicate])
a1 = np.arange(10)
print(a1)
print(a1[predicate])
print(a1[rnd > 0.5])
print(a1[(rnd > 0.5) & (a1 < 5)])


